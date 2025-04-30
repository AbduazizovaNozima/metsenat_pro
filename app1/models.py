from django.db import models
from helper.choices import StatusChoices, PaymentChoices, UserTypeChoices
from django.core.validators import RegexValidator

class BaseModel(models.Model):
    objects = models.Manager()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Position(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Student(BaseModel):
    full_name = models.CharField(max_length=255)
    phone_validator = RegexValidator(
        regex=r'^\+998\d{9}$',
        message="Telefon raqami +998 bilan boshlanib, jami 13 ta raqamdan iborat bo‘lishi kerak (masalan: +998901234567)"
    )
    phone = models.CharField(
        max_length=13,
        null=False,
        blank=False,
        validators=[phone_validator]
    )
    status = models.CharField(
        max_length=100,
        choices=StatusChoices.choices,
        default=StatusChoices.BACHELOR
    )
    OTM = models.CharField(max_length=255)
    separated_amount = models.BigIntegerField(default=0)
    contract = models.BigIntegerField()

    def formatted_separated_amount(self):
        return f"{self.separated_amount:,.0f} UZS".replace(",", " ")

    def formatted_contract(self):
        return f"{self.contract:,.0f} UZS".replace(",", " ")


    def __str__(self):
        return self.full_name


class Sponsor(BaseModel):
    full_name = models.CharField(max_length=255)
    phone_validator = RegexValidator(
        regex=r'^\+998\d{9}$',
        message="Telefon raqami +998 bilan boshlanib, jami 13 ta raqamdan iborat bo‘lishi kerak (masalan: +998901234567)"
    )
    phone = models.CharField(
        max_length=13,
        validators=[phone_validator]
    )
    sponsor_amount = models.BigIntegerField()
    spent_amount = models.BigIntegerField()
    date = models.DateField()
    position = models.ForeignKey(
        Position, on_delete=models.CASCADE,
        related_name='sponsors'
    )
    student = models.ForeignKey(
        Student, on_delete=models.CASCADE,
        related_name='sponsors'
    )
    payment = models.CharField(
        max_length=100,
        choices=PaymentChoices.choices
    )
    user_type = models.CharField(
        max_length=100,
        choices=UserTypeChoices.choices,
        default=UserTypeChoices.INDIVIDUAL
    )
    workplace = models.CharField(max_length=200, blank=True, null=True)

    def formatted_sponsor_amount(self):
        return f"{self.sponsor_amount:,.0f} UZS".replace(",", " ")

    def formatted_spent_amount(self):
        return f"{self.spent_amount:,.0f} UZS".replace(",", " ")

    def __str__(self):
        return self.full_name


