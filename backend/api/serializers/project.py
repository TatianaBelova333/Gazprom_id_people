from django.db.models import Case, When, F
from rest_framework import serializers

from apps.projects.models import Project
from apps.staff.models import Employee
from api.serializers.position import PositionSerializer
from api.serializers.progress_status import ProgressStatusSerializer
from api.serializers.tag import WorkTagSerializer
from api.serializers.team_member import TeamMemberSerializer
from api.utils import check_start_date_lt_end_date, get_team_groups


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


class ProjectListSerializer(serializers.ModelSerializer):
    '''
    Serializer for listing all company projects (Раздел 'Проекты').

    '''
    director = TeamMemberSerializer()
    company_teams = serializers.SerializerMethodField()
    status = ProgressStatusSerializer()

    class Meta:
        model = Project
        fields = (
            'id',
            'name',
            'status',
            'company_teams',
            'director',
        )

    def get_company_teams(self, project):
        '''Return project members grouped by company teams(отделы).'''
        return get_team_groups(project)


class ProjectDetailSerializer(ProjectListSerializer):
    '''
    Serializer for information about a single project.

    '''
    tags = WorkTagSerializer(many=True)

    class Meta(ProjectListSerializer.Meta):
        model = Project
        fields = ProjectListSerializer.Meta.fields + (
            'tags',
            'description',
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

        check_start_date_lt_end_date(start_date=start_date, end_date=end_date)

        return data

    def to_representation(self, project) -> ProjectDetailSerializer:
        return ProjectDetailSerializer(project).data
