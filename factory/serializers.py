from rest_framework import serializers
from .models import PreRequestIDC, PreRequestPassport
        
class PreRequestIDCSerializer(serializers.HyperlinkedModelSerializer):
    author = serializers.PrimaryKeyRelatedField(read_only=True, many=False)
    corrector = serializers.PrimaryKeyRelatedField(read_only=True, many=False)
    identity_card = serializers.PrimaryKeyRelatedField(read_only=True, many=False)
    class Meta:
        model = PreRequestIDC
        read_only_fields = ('url', 'id', 'author', 'corrector', 'date_of_creation', 
                            'validation', 'number', 'identity_card')
        fields= ['id', 'first_name', 'last_name', 'sexe', 'date_of_birth','place_of_birth', 'adress',
                 'number', 'date_of_creation', 'author', 'corrector', 'validation', 'identity_card']

class PreRequestPassportSerializer(serializers.HyperlinkedModelSerializer):
    author = serializers.PrimaryKeyRelatedField(read_only=True, many=False)
    corrector = serializers.PrimaryKeyRelatedField(read_only=True, many=False)
    passport = serializers.PrimaryKeyRelatedField(read_only=True, many=False)
    class Meta:
        model = PreRequestPassport
        read_only_fields = ('url', 'id', 'author', 'corrector', 'date_of_creation',
                            'validation', 'number', 'passport')
        fields= ['id', 'first_name', 'last_name', 'sexe', 'date_of_birth','place_of_birth',
                 'height', 'type',
                 'number', 'date_of_creation', 'author', 'corrector', 'validation', 'passport']
