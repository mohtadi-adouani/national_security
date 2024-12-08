from rest_framework import viewsets, mixins
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import PreRequestIDCSerializer, PreRequestPassportSerializer
from .models import PreRequestIDC, PreRequestPassport
from .tasks import create_identity_card, create_passport

class PreRequestIDCViewSet(mixins.CreateModelMixin,
                            mixins.ListModelMixin,
                            viewsets.GenericViewSet):
    queryset = PreRequestIDC.objects.all()
    serializer_class = PreRequestIDCSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    @action(detail=True, methods=['post'])
    def validate(self, request, pk=None):
        pre_req_idc = self.get_object()
        pre_req_idc.validate(request.user)
        create_identity_card.delay(pre_req_idc.pk)

        return Response(data=PreRequestIDCSerializer(pre_req_idc).data)


class PreRequestPassportViewSet(mixins.CreateModelMixin,
                            mixins.ListModelMixin,
                            viewsets.GenericViewSet):
    queryset = PreRequestPassport.objects.all()
    serializer_class = PreRequestPassportSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    @action(detail=True, methods=['post'])
    def validate(self, request, pk=None):
        pre_req_passport = self.get_object()
        pre_req_passport.validate(request.user)
        create_passport.delay(pre_req_passport.pk)

        return Response(data=PreRequestPassportSerializer(pre_req_passport).data)