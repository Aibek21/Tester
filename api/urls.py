from django.conf.urls import include, url

from . import views
from rest_framework import routers, serializers, viewsets
from django.contrib.auth.models import User
from .views import UserViewSet, VariantViewSet


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'variants', VariantViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
]