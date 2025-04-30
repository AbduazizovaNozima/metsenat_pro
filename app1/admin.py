from django.contrib import admin
from . import models


@admin.register(models.Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id','full_name', 'status', 'OTM', 'formatted_separated_amount', 'formatted_contract')
    search_fields = ('full_name', 'OTM')
    list_filter = ('OTM', 'status')
    readonly_fields = ('created_at', 'updated_at')


@admin.register(models.Sponsor)
class SponsorAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'phone', 'formatted_sponsor_amount', 'formatted_spent_amount', 'date', 'payment')
    search_fields = ('full_name', 'phone')
    list_filter = ('position', 'date', 'sponsor_amount')


@admin.register(models.Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)



