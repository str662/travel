from django.contrib import admin

from .models import ProfileModel


@admin.register(ProfileModel)
class BuyAdmin(admin.ModelAdmin):
    list_display = ['user']
