from rest_framework import serializers

from apps.company_structure.models import Position


class PositionSerializer(serializers.ModelSerializer):
    '''Serializer for employee positions.'''

    class Meta:
        model = Position
        fields = ('id', 'name')
