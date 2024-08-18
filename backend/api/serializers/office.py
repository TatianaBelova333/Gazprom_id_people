from rest_framework import serializers

from apps.company_structure.models import CompanyOffice


class OfficeSerializer(serializers.ModelSerializer):
    '''Serializer for company offices.'''

    class Meta:
        model = CompanyOffice
        fields = ('id', 'address')
