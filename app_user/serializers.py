from rest_framework import serializers
from . import models


class RegisterSerializer(serializers.Serializer):
    full_name = serializers.CharField(max_length=255, required=True, write_only=True)
    phone = serializers.CharField(max_length=255, required=True, write_only=True)
    password = serializers.CharField(max_length=255, required=True, write_only=True)


    def create(self, validated_data):
        full_name = validated_data.get('full_name')
        phone = validated_data.get('phone')
        password = validated_data.get('password')
        login = validated_data.get('login')

        user = models.CustomUser.objects.filter(phone=phone).first()

        if user:

            user.full_name = full_name
            user.password = password
            user.login = login
            user.save()

            return user

        else:
            user = models.CustomUser.objects.create_user(
                phone=phone, password=password, full_name=full_name
            )

            return user
