from rest_framework import serializers

from api.serializers.progress_status import ProgressStatusSerializer
from api.serializers.tag import WorkTagSerializer
from api.utils import (
    check_dates_within_project_dates,
    check_start_date_lt_end_date,
    check_team_members_belong_to_project,
    get_team_groups,
)
from apps.projects.models import Component


class ComponentListSerializer(serializers.ModelSerializer):
    '''Serialiser for listing all components.'''

    class Meta:
        model = Component
        fields = (
            'id',
            'name',
            'start_date',
            'end_date',
        )


class ComponentDetailSerializer(serializers.ModelSerializer):
    '''Serialiser for retrieving a single component.'''
    tags = WorkTagSerializer(many=True)
    status = ProgressStatusSerializer()
    company_teams = serializers.SerializerMethodField()
    priority = serializers.ChoiceField(
        choices=Component.Priority
    )

    class Meta:
        model = Component
        fields = (
            'id',
            'name',
            'description',
            'status',
            'start_date',
            'end_date',
            'tags',
            'release_type',
            'priority',
            'service',
            'company_teams',
        )

    def get_company_teams(self, component):
        '''Return component members grouped by company teams(отделы).'''
        return get_team_groups(component)


class ComponentCreateUpdateSerializer(serializers.ModelSerializer):
    '''Serializer for creating and updating components.'''

    class Meta:
        model = Component
        fields = (
            'service',
            'name',
            'description',
            'status',
            'tags',
            'team_members',
            'start_date',
            'end_date',
            'priority',
            'release_type',
        )
        read_only_fields = ('id',)
        extra_kwargs = {
            'service': {'required': True},
            'description': {'required': True, 'allow_blank': False},
            'name': {'required': True, 'allow_blank': False},
        }

    def validate(self, data):
        '''
        Validate that end_date is greater than start_date
        and component dates are within the related project dates.

        '''
        # service is a required field and each service belogns to a project
        service = data['service']
        project = service.project

        component_start_date = data.get('start_date')
        component_end_date = data.get('end_date')

        check_start_date_lt_end_date(
            start_date=component_start_date,
            end_date=component_end_date,
        )
        check_dates_within_project_dates(
            start_date=component_start_date,
            end_date=component_end_date,
            project=project,
        )

        component_members = data.get('team_members')

        check_team_members_belong_to_project(
            members=component_members,
            project=project,
        )
        return data

    def to_representation(self, service) -> ComponentDetailSerializer:
        return ComponentDetailSerializer(service).data
