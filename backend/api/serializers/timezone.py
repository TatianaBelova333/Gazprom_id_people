from rest_framework import serializers

from apps.staff.models import EmployeeTimeZone


class EmployeeTimeZoneSerializer(serializers.ModelSerializer):
    '''Serializer for employee timezones.'''

    class Meta:
        model = EmployeeTimeZone
        fields = ('id', 'name')
