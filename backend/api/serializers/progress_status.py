from rest_framework import serializers

from apps.projects.models import ProgressStatus


class ProgressStatusSerializer(serializers.ModelSerializer):
    '''Serializer for work progress statuses.'''

    class Meta:
        model = ProgressStatus
        fields = ('id', 'name', 'color')
