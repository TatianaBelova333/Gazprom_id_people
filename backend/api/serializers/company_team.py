from rest_framework import serializers

from apps.company_structure.models import CompanyTeam


class CompanyTeamBriefInfoSerializer(serializers.ModelSerializer):
    '''Serializer for company teams.'''

    class Meta:
        model = CompanyTeam
        fields = ('id', 'name')
