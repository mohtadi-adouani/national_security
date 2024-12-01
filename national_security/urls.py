from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from identity_card.views import IdentityCardViewSet, PassportViewSet
from factory.views import PreRequestIDCViewSet
from .views import UserViewSet

router = routers.DefaultRouter()
router.register(r'prerequestidc', PreRequestIDCViewSet)
router.register(r'idc', IdentityCardViewSet)
router.register(r'passport', PassportViewSet)
router.register(r'users', UserViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
