from rest_framework import serializers

from api.serializers.progress_status import ProgressStatusSerializer
from api.serializers.tag import WorkTagSerializer
from api.utils import get_team_groups
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
        service = data['service']
        project = service.project
        project_start_date = project.start_date
        project_end_date = project.end_date

        component_start_date = data.get('start_date')
        component_end_date = data.get('end_date')

        if component_start_date:
            if (project_start_date
                    and component_start_date < project_start_date):
                raise serializers.ValidationError(
                    (f'Дата начала компонента не может быть раньше '
                     f'даты начала проекта {project_start_date}.')
                )
            if project_end_date and component_start_date > project_end_date:
                raise serializers.ValidationError(
                    (f'Дата начала компонента не может быть позже '
                     f'даты окончания проекта {project_end_date}.')
                )

        if component_end_date:
            if project_end_date and component_end_date > project_start_date:
                raise serializers.ValidationError(
                    (f'Дата окончания компонента не может быть позже '
                     f'даты окончания проекта {project_end_date}.')
                )
            if project_start_date and component_end_date < project_start_date:
                raise serializers.ValidationError(
                    (f'Дата окончания компонента не может быть раньше '
                     f'даты начала проекта {project_start_date}.')
                )

        if component_start_date and component_end_date:
            if component_start_date >= component_end_date:
                raise serializers.ValidationError(
                    'Дата начала компонента не может быть позже даты окончания.'
                )

        component_members = data.get('team_members')

        if component_members:
            project_members = set(project.team_members.all())
            project_director = project.director
            if project_director:
                project_members.add(project_director)

            if not set(component_members).issubset(project_members):
                raise serializers.ValidationError(
                    ('Участники команды компонента должны '
                     'входить в команду проекта.')
                )
        return data

    def to_representation(self, service) -> ComponentDetailSerializer:
        return ComponentDetailSerializer(service).data
