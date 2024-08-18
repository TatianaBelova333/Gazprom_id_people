from rest_framework import serializers

from apps.projects.models import WorkTag


class WorkTagSerializer(serializers.ModelSerializer):
    '''Serializer for work tags.'''

    class Meta:
        model = WorkTag
        fields = ('id', 'name', 'color')
