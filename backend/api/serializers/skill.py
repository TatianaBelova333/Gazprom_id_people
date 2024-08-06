from rest_framework import serializers

from apps.staff.models import Skill


class SkillSerializer(serializers.ModelSerializer):
    """Serializer for employee's skills."""

    class Meta:
        model = Skill
        fields = ('id', 'name', 'color')
