from rest_framework import serializers

from apps.staff.models import SavedContact


class SavedContactSerializer(serializers.ModelSerializer):
    '''Serialiser for the employee's saved contacts.'''
    user_id = serializers.IntegerField(source='contact.id')
    full_name = serializers.CharField(source='contact.get_full_name')
    phone_number = serializers.CharField(source='contact.phone_number')
    email = serializers.EmailField(source='contact.email')
    image = serializers.URLField(source='contact.image')
    telegram = serializers.CharField(source='contact.telegram')
    employment_type = serializers.IntegerField(
        source='contact.employment_type'
    )
    ms_teams = serializers.EmailField(source='contact.ms_teams')
    position = serializers.CharField(source='contact.position')

    class Meta:
        model = SavedContact
        fields = [
            'user_id',
            'full_name',
            'position',
            'phone_number',
            'telegram',
            'email',
            'image',
            'employment_type',
            'telegram',
            'ms_teams',
        ]
