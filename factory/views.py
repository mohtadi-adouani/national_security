from rest_framework import viewsets, mixins
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import PreRequestIDCSerializer
from .models import PreRequestIDC


class PreRequestIDCViewSet(mixins.CreateModelMixin,
                            mixins.ListModelMixin,
                            viewsets.GenericViewSet):
    queryset = PreRequestIDC.objects.all()
    serializer_class = PreRequestIDCSerializer

    @action(detail=True, methods=['post'])
    def validate(self, request, pk=None):
        pre_req_idc = self.get_object()
        pre_req_idc.validate(request.user)
        return Response(data=PreRequestIDCSerializer(pre_req_idc).data)