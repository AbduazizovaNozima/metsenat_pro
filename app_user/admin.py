from django.contrib import admin
from .models import CustomUser, CodeVerification

admin.site.register(CustomUser)
admin.site.register(CodeVerification)