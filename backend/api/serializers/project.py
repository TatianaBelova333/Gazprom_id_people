from rest_framework import serializers

from apps.projects.models import Project
from apps.staff.models import Employee
from api.serializers.company_team import CompanyTeamBriefInfoSerializer
from api.serializers.position import PositionSerializer
from api.serializers.progress_status import ProgressStatusSerializer
from api.serializers.tag import WorkTagSerializer


class ProjectNameSerializer(serializers.ModelSerializer):
    '''Serialiser for listing employee projects in the employee catalogue.'''

    class Meta:
        model = Project
        fields = (
            'id',
            'name',
        )


class ProjectDirectorSerializer(serializers.ModelSerializer):
    '''Serializer for project directors on the main page.'''
    full_name = serializers.CharField(source='get_full_name')
    position = PositionSerializer()

    class Meta:
        model = Employee
        fields = (
            'id',
            'full_name',
            'position',
            'phone_number',
            'telegram',
            'email',
            'image',
            'employment_type',
            'telegram',
            'ms_teams',
            'position',
        )


class ProjectMemberMainPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('id', 'image', 'employment_type')


class ProjectMainPageSerializer(serializers.ModelSerializer):
    '''
    Serializer for listing the current user's projects on the main page.

    '''
    director = ProjectDirectorSerializer(many=False)
    tags = WorkTagSerializer(many=True)
    status = ProgressStatusSerializer()
    team_members = serializers.SerializerMethodField()
    team_extra_count = serializers.SerializerMethodField()

    class Meta:
        model = Project
        fields = (
            'id',
            'name',
            'description',
            'status',
            'start_date',
            'end_date',
            'tags',
            'team_members',
            'team_extra_count',
            'director',
        )

    def _get_team_limit(self):
        '''Return the value of `team_limit` query_param or 0.'''
        request = self.context.get('request')
        if request:
            team_limit = int(request.query_params.get('team_limit', 0))
            return team_limit
        return 0

    def get_team_members(self, project) -> ProjectMemberMainPageSerializer:
        '''
        Return a list of project team members limited
        by `team_limit` query_param.

        '''
        queryset = project.team_members.all()

        team_limit = self._get_team_limit()
        if team_limit > 0:
            queryset = queryset[:team_limit]

        serializer = ProjectMemberMainPageSerializer(
            queryset,
            many=True,
            read_only=True
        )
        return serializer.data

    def get_team_extra_count(self, obj) -> int:
        '''
        Return the difference between the total number of team members
        and the `team_limit` query_param.

        '''
        team_limit = self._get_team_limit()
        if team_limit == 0:
            return 0

        all_members_count = obj.team_members.count()
        team_extra_count = all_members_count - team_limit
        return team_extra_count if team_extra_count > 0 else 0


class TeamMemberSerializer(serializers.ModelSerializer):
    '''
    Serializer for listing team members of projects, services and components.

    '''
    position = PositionSerializer()
    company_team = serializers.SerializerMethodField()

    class Meta:
        model = Employee
        fields = (
            'id',
            'image',
            'last_name',
            'first_name',
            'employment_type',
            'position',
            'company_team',
        )

    def get_company_team(self, employee) -> CompanyTeamBriefInfoSerializer:
        '''Return the company team (Отдел) that employee belongs to.'''

        unit = employee.unit
        if unit is not None:
            return CompanyTeamBriefInfoSerializer(unit.team).data

        if hasattr(employee, 'team'):
            return CompanyTeamBriefInfoSerializer(employee.team).data


class ProjectListSerializer(serializers.ModelSerializer):
    '''
    Serializer for listing all company projects (Раздел 'Проекты').

    '''
    director = TeamMemberSerializer()
    team_members = TeamMemberSerializer(many=True)
    status = ProgressStatusSerializer()

    class Meta:
        model = Project
        fields = (
            'id',
            'name',
            'status',
            'team_members',
            'director',
        )


class ProjectDetailSerializer(serializers.ModelSerializer):
    '''
    Serializer for information about a single project.

    '''
    director = TeamMemberSerializer()
    team_members = TeamMemberSerializer(many=True)
    tags = WorkTagSerializer(many=True)
    status = ProgressStatusSerializer()

    class Meta:
        model = Project
        fields = (
            'id',
            'name',
            'status',
            'description',
            'tags',
            'team_members',
            'director',
            'start_date',
            'end_date',
        )


class ProjectCreateUpdateSerializer(serializers.ModelSerializer):
    '''Serializer for creating/updating projects.'''

    class Meta:
        model = Project
        fields = (
            'name',
            'status',
            'description',
            'tags',
            'team_members',
            'director',
            'start_date',
            'end_date',
        )
        extra_kwargs = {
            'description': {'required': True, 'allow_blank': False},
            'name': {'required': True, 'allow_blank': False},
        }

    def validate(self, data):
        '''
        Validate that end_date is greater than start_date.
        Check and remove project director from project team members.

        '''
        start_date = data.get('start_date')
        end_date = data.get('end_date')

        if (start_date and end_date) and (start_date >= end_date):
            raise serializers.ValidationError(
                'Дата начала не может быть позже даты окончания.'
            )

        return data

    def to_representation(self, project) -> ProjectDetailSerializer:
        return ProjectDetailSerializer(project).data
