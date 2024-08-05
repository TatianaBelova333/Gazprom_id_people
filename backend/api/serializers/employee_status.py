from rest_framework import serializers

from apps.staff.models import EmployeeStatus


class EmployeeStatusSerializer(serializers.ModelSerializer):
    """Serializer for employee's statuses."""

    class Meta:
        model = EmployeeStatus
        fields = ('id', 'name', 'color')
