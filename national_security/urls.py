from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from identity_card.views import IdentityCardViewSet, PassportViewSet
from factory.views import PreRequestIDCViewSet, PreRequestPassportViewSet
from .views import UserViewSet

router = routers.DefaultRouter()
router.register(r'pre_request_idc', PreRequestIDCViewSet)
router.register(r'pre_request_passport', PreRequestPassportViewSet)
router.register(r'idc', IdentityCardViewSet)
router.register(r'passport', PassportViewSet)
router.register(r'users', UserViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth')
]