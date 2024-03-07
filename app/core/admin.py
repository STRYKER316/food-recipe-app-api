""" Django admin customization """

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as translate

from core import models


class CustomUserAdmin(UserAdmin):
    """ Define admin page for user model """
    ordering = ['id']
    list_display = ['email', 'name']

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (
            translate('Permissions'),
            {
                'fields': (
                    'is_active',
                    'is_staff',
                    'is_superuser'
                )
            }
        ),
        (translate('Important dates'), {'fields': ('last_login',)}),
    )
    readonly_fields = ['last_login']


# Register your models here.
admin.site.register(models.User, CustomUserAdmin)
