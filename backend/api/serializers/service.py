from rest_framework import serializers

from api.serializers.progress_status import ProgressStatusSerializer
from api.serializers.tag import WorkTagSerializer
from api.utils import get_team_groups
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
        project = data['project']
        project_start_date = project.start_date
        project_end_date = project.end_date

        service_start_date = data.get('start_date')
        service_end_date = data.get('end_date')

        if service_start_date:
            if project_start_date and service_start_date < project_start_date:
                raise serializers.ValidationError(
                    (f'Дата начала сервиса не может быть раньше '
                     f'даты начала проекта {project_start_date}.')
                )
            if project_end_date and service_start_date > project_end_date:
                raise serializers.ValidationError(
                    (f'Дата начала сервиса не может быть позже '
                     f'даты окончания проекта {project_end_date}.')
                )

        if service_end_date:
            if project_end_date and service_end_date > project_start_date:
                raise serializers.ValidationError(
                    (f'Дата окончания сервиса не может быть позже '
                     f'даты окончания проекта {project_end_date}.')
                )
            if project_start_date and service_end_date < project_start_date:
                raise serializers.ValidationError(
                    (f'Дата окончания сервиса не может быть раньше '
                     f'даты начала проекта {project_start_date}.')
                )

        if service_start_date and service_end_date:
            if service_start_date >= service_end_date:
                raise serializers.ValidationError(
                    'Дата начала сервиса не может быть позже даты окончания.'
                )

        service_members = data.get('team_members')

        if service_members:
            project_members = set(project.team_members.all())
            project_director = project.director
            if project_director:
                project_members.add(project_director)

            if not set(service_members).issubset(project_members):
                raise serializers.ValidationError(
                    ('Участники команды сервиса должны '
                     'входить в команду проекта.')
                )
        return data

    def to_representation(self, service) -> ServiceDetailSerializer:
        return ServiceDetailSerializer(service).data
