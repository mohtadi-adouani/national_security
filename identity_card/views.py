from rest_framework import viewsets
from .serializers import IdentityCardSerializer
from .models import IdentityCard

class IdentityCardViewSet(viewsets.ModelViewSet):
    queryset = IdentityCard.objects.all()
    serializer_class = IdentityCardSerializer