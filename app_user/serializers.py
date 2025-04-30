from rest_framework import serializers
from . import models
import random


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
            user.save()

            verification = models.CodeVerification.objects.filter(
                user=user
            )
            verification.delete()
            self.create_verify_code(user)

            return user

        else:
            user = models.CustomUser.objects.create_user(
                phone=phone, password=password, full_name=full_name
            )

            self.create_verify_code(user)

            return user

    @classmethod
    def create_verify_code(cls, user):
        code = cls.generate_random_number()
        models.CodeVerification.objects.create(
            user=user, code=code
        )

    @staticmethod
    def generate_random_number():
        return ''.join([str(random.randint(0,9)) for _ in range(4)])

