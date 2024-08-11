from rest_framework import serializers

from apps.company_structure.models import CompanyUnit


class CompanyUnitBriefInfoSerializer(serializers.ModelSerializer):
    '''Serializer for company units.'''

    class Meta:
        model = CompanyUnit
        fields = ('id', 'name')
