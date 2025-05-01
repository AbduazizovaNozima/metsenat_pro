from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import CustomUser

class LoginSerializer(serializers.Serializer):
    login = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        login = data.get('login')
        password = data.get('password')

        try:
            user = CustomUser.objects.get(login=login)
        except CustomUser.DoesNotExist:
            raise serializers.ValidationError("Login noto‘g‘ri")

        if not user.check_password(password):
            raise serializers.ValidationError("Parol noto‘g‘ri")

        if not user.is_active:
            raise serializers.ValidationError("Foydalanuvchi aktiv emas")

        data['user'] = user
        return data
