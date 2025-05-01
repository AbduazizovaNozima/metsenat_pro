from django.contrib.auth.models import AbstractBaseUser, UserManager, PermissionsMixin
from django.db import models
from django.core.validators import RegexValidator
from django.utils import timezone


class CustomUserManager(UserManager):
    def _create_user(self, phone, login, password, **extra_fields):
        if not phone:
            raise ValueError('Phone not found')

        user = self.model(phone=phone, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_user(self, phone=None, login=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(phone, login, password, **extra_fields)

    def create_superuser(self, phone=None, login=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(phone, login, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    phone_validator = RegexValidator(
        regex=r'^\+998(9[0-9]|3[3]|7[1])\d{7}$',
        message="Telefon raqamingiz +998 bilan boshlanib, jami 13 ta raqamdan iborat bo‘lishi kerak. Masalan: +998901234567"
    )

    phone = models.CharField(
        max_length=13,
        unique=True,
        validators=[phone_validator]
    )
    login = models.CharField(
        max_length=150,
        unique=True,
        null=True,
        blank=True
    )

    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    date_joined = models.DateTimeField(default=timezone.now)
    last_login = models.DateTimeField(blank=True, null=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'phone'

    REQUIRED_FIELDS = ['login']

    class Meta:
        verbose_name = 'CustomUser'
        verbose_name_plural = 'CustomUsers'


