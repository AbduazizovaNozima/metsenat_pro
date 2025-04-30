from rest_framework import generics
from . import serializers
from .models import *


class RegisterAPIView(generics.CreateAPIView):
    serializer_class = serializers.RegisterSerializer
    queryset = CustomUser.objects.all()
