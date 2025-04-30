from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from helper.choices import *
# import re


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects=models.Manager()

    class Meta:
        abstract = True


class CustomerUserManager(BaseUserManager):
    def create_user(self, phone, password, **extra_fields):
        if not phone:
            raise ValueError({"phone": "MISTAKE"})

        user = self.model(phone=phone, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(phone, password, **extra_fields)


class CustomUser(AbstractUser):

    STATUS_CHOICES = [
        (NEW, 'New'),
        (ACTIVE, 'Active')
    ]

    username = None
    first_name = None
    last_name = None
    email = None

    status = models.CharField(max_length=255, choices=STATUS_CHOICES, default=NEW)
    phone = models.CharField(max_length=255, unique=True)
    full_name = models.CharField(max_length=255, null=True)
    login = models.CharField(max_length=255, null=True)

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = ['full_name']

    objects = CustomerUserManager()







