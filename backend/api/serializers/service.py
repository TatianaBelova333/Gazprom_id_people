from rest_framework import serializers

from api.serializers.progress_status import ProgressStatusSerializer
from api.serializers.tag import WorkTagSerializer
from api.utils import (
    check_dates_within_project_dates,
    check_start_date_lt_end_date,
    check_team_members_belong_to_project,
    get_team_groups,
)
from apps.projects.models import Service


class ServiceListSerializer(serializers.ModelSerializer):
    '''Serialiser for listing all services.'''

    class Meta:
        model = Service
        fields = (
            'id',
            'name',
            'start_date',
            'end_date',
        )


class ServiceDetailSerializer(serializers.ModelSerializer):
    '''
    Serializer for return information about a single service.

    '''
    company_teams = serializers.SerializerMethodField()
    tags = WorkTagSerializer(many=True)
    status = ProgressStatusSerializer()

    class Meta:
        model = Service
        fields = (
            'id',
            'project',
            'name',
            'status',
            'description',
            'tags',
            'company_teams',
            'start_date',
            'end_date',
        )

    def get_company_teams(self, service):
        '''Return service members grouped by company teams(отделы).'''
        return get_team_groups(service)


class ServiceCreateUpdateSerializer(serializers.ModelSerializer):
    '''Serializer for creating and updating services.'''

    class Meta:
        model = Service
        fields = (
            'project',
            'name',
            'description',
            'status',
            'tags',
            'team_members',
            'start_date',
            'end_date',
        )
        read_only_fields = ('id',)
        extra_kwargs = {
            'project': {'required': True},
            'description': {'required': True, 'allow_blank': False},
            'name': {'required': True, 'allow_blank': False},
        }

    def validate(self, data):
        '''
        Validate that end_date is greater than start_date
        and service dates are within the related project dates.

        '''
        # project is a required field
        project = data['project']

        service_start_date = data.get('start_date')
        service_end_date = data.get('end_date')

        check_start_date_lt_end_date(
            start_date=service_start_date,
            end_date=service_end_date
        )
        check_dates_within_project_dates(
            start_date=service_start_date,
            end_date=service_end_date,
            project=project,
        )

        service_members = data.get('team_members')

        check_team_members_belong_to_project(
            members=service_members,
            project=project,
        )

        return data

    def to_representation(self, service) -> ServiceDetailSerializer:
        return ServiceDetailSerializer(service).data
