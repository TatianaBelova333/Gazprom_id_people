from rest_framework import serializers

from apps.projects.models import Project
from apps.staff.models import Employee
from api.serializers import ProgressStatusSerializer, WorkTagSerializer


class DirectorSerializer(serializers.ModelSerializer):
    full_name = serializers.CharField(source='get_full_name')
    position = serializers.CharField(source='position.name')

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


class TeamMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('id', 'image')


class ProjectMainPageSerializer(serializers.ModelSerializer):
    '''
    Serializer for a list of the current user's projects on the main page.

    '''
    director = DirectorSerializer(many=False)
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

    def get_team_members(self, obj) -> TeamMemberSerializer:
        '''
        Return a list of project team members limited
        by `team_limit` query_param.

        '''
        queryset = obj.team_members.all()

        team_limit = self._get_team_limit()
        if team_limit > 0:
            queryset = queryset[:team_limit]

        serializer = TeamMemberSerializer(queryset, many=True, read_only=True)
        return serializer.data

    def get_team_extra_count(self, obj) -> int:
        '''
        Return the difference between the total number of team members
        and the `team_limit` query_param.

        '''
        team_limit = self._get_team_limit()
        all_members_count = obj.team_members.count()
        team_extra_count = all_members_count - team_limit
        if team_extra_count > 0:
            return team_extra_count
        return 0
