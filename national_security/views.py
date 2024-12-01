from rest_framework import viewsets, mixins
from .serializers import UserSerializer
from django.contrib.auth.models import User


class UserViewSet(mixins.ListModelMixin,
                  viewsets.GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer