from .serializers import UserSerializer, VariantDetailSerializer, VariantListSerializer
from testapp.models import Question, Answer, Task, Variant
import re
from django.conf import settings
import os
from rest_framework import viewsets
from django.contrib.auth.models import User


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class VariantViewSet(viewsets.ReadOnlyModelViewSet):
	queryset = Variant.objects.all()
	def get_serializer_class(self):
		if self.action == 'retrieve':
			return VariantDetailSerializer
		if self.action == 'list':
			return VariantListSerializer