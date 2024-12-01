from rest_framework import viewsets, mixins
from .serializers import PreRequestIDCSerializer
from .models import PreRequestIDC

class PreRequestIDCViewSet(mixins.CreateModelMixin,
                            mixins.ListModelMixin,
                            viewsets.GenericViewSet):
    queryset = PreRequestIDC.objects.all()
    serializer_class = PreRequestIDCSerializer