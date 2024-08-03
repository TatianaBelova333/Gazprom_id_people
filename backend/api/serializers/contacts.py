from rest_framework import serializers

from apps.staff.models import SavedContact


class SavedContactSerializer(serializers.ModelSerializer):
    """Serialiser for the saved contacts."""
    user_id = serializers.CharField(source='contact.id')
    full_name = serializers.CharField(source='contact.get_full_name')
    phone_number = serializers.CharField(source='contact.phone_number')
    email = serializers.CharField(source='contact.email')
    image = serializers.CharField(source='contact.image')
    telegram = serializers.CharField(source='contact.telegram')

    class Meta:
        model = SavedContact
        fields = [
            'user_id',
            'full_name',
            # 'position',
            'phone_number',
            'email',
            'image',
            # 'state',
            'telegram',
            #  'msteams',
        ]
