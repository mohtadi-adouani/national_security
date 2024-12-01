from rest_framework import serializers
from .models import PreRequestIDC
from django.contrib.auth.models import User

        
class PreRequestIDCSerializer(serializers.HyperlinkedModelSerializer):
    # author = serializers.PrimaryKeyRelatedField(read_only=True, many=False)
    author = serializers.PrimaryKeyRelatedField(read_only=True, many=False)
    corrector = serializers.PrimaryKeyRelatedField(read_only=True, many=False)
    class Meta:
        model = PreRequestIDC
        read_only_fields = ('url', 'id', 'author', 'corrector', 'date_of_creation', 
                            'validation', 'number')
        fields= ['id', 'first_name', 'last_name', 'sexe', 'date_of_birth','place_of_birth', 'adress',
                 'number', 'date_of_creation', 'author', 'corrector', 'validation']
