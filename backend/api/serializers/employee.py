from django.contrib.auth import get_user_model
from djoser.serializers import UserSerializer
from rest_framework import serializers

from apps.staff.models import EmployeeStatus, SavedContact, Skill


Employee = get_user_model()


class StatusSerializer(serializers.ModelSerializer):
    """Serializer for Employee's work status."""

    class Meta:
        model = EmployeeStatus
        fields = ('id', 'name', 'color')


class SkillSerializer(serializers.ModelSerializer):
    """Serializer for Employee's skills."""

    class Meta:
        model = Skill
        fields = ('id', 'name', 'color')


class EmployeeSerializer(UserSerializer):
    """Serialiser for Employee's profile."""
    is_saved_contact = serializers.SerializerMethodField()
    office = serializers.StringRelatedField(read_only=True)
    status = StatusSerializer()
    skills = SkillSerializer(many=True, read_only=True)

    class Meta:
        model = Employee
        fields = [
            'id',
            'first_name',
            'last_name',
            'middle_name',
            'birthday',
            'office',
            'phone_number',
            'email',
            'status',
            'skills',
            'image',
            'is_saved_contact',
            'employment_type',
            # position,
        ]

    def get_is_saved_contact(self, obj):
        request = self.context.get('request')
        if request:
            request_user = request.user
            other_user = obj.id
            return (request_user.is_authenticated
                    and SavedContact.objects.filter(
                        employee=request_user,
                        contact=other_user
                    ).exists())
        return False
