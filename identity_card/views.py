from rest_framework import viewsets
from .serializers import IdentityCardSerializer, PassportSerializer
from .models import IdentityCard, Passport

class IdentityCardViewSet(viewsets.ModelViewSet):
    queryset = IdentityCard.objects.all()
    serializer_class = IdentityCardSerializer

class PassportViewSet(viewsets.ModelViewSet):
    queryset = Passport.objects.all()
    serializer_class = PassportSerializer