from rest_framework import serializers
from .models import IdentityCard

# Serializers define the API representation.
class IdentityCardSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = IdentityCard
        fields = ['url', 'first_name', 'last_name', 'date_of_birth', 'place_of_birth',
                  'adress','number',
                  'date_of_creation', 'expiry_date']