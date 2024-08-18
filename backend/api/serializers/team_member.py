from rest_framework import serializers

from apps.staff.models import Employee
from api.serializers.position import PositionSerializer


class TeamMemberSerializer(serializers.ModelSerializer):
    '''
    Serializer for team members of projects, services and components.

    '''
    position = PositionSerializer()

    class Meta:
        model = Employee
        fields = (
            'id',
            'image',
            'last_name',
            'first_name',
            'employment_type',
            'position',
        )