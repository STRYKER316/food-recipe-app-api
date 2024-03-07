""" Django admin customization """

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from core import models


class CustomUserAdmin(BaseUserAdmin):
    """ Define admin page for user model """
    ordering = ['id']
    list_display = ['email', 'name']


# Register your models here.
admin.site.register(models.User, CustomUserAdmin)
