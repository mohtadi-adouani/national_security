from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .serializers import IdentityCardSerializer, PassportSerializer
from .models import IdentityCard, Passport

class IdentityCardViewSet(viewsets.ModelViewSet):
    queryset = IdentityCard.objects.all()
    serializer_class = IdentityCardSerializer
    @action(detail=True, methods=['post'])
    def activate(self, request, pk=None):
        idc = self.get_object()
        idc.activate()
        return Response(data=IdentityCardSerializer(idc, context={'request': request}).data)

class PassportViewSet(viewsets.ModelViewSet):
    queryset = Passport.objects.all()
    serializer_class = PassportSerializer

    @action(detail=True, methods=['post'])
    def activate(self, request, pk=None):
        passport = self.get_object()
        passport.activate()
        return Response(data=PassportSerializer(passport, context={'request': request}).data)