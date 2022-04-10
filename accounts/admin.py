from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from django.db import models
from .models import User


# Register your models here.

class AccountAdminConfig(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'date_joined', 'last_login', 'is_active')
    list_display_links = ('username', 'email')
    readonly_fields = ('last_login', 'date_joined')
    ordering = ('-date_joined',)

    filter_horizontal = ()
    list_filter = ()
    fieldsets = (
        (None, {'fields': ('email', 'username', 'first_name', 'last_name', 'phone_number')}),
        ('Permissions', {'fields': ('is_staff', 'is_admin', 'is_superadmin', 'is_active')}),
        ('Log', {'fields': ('date_joined', 'last_login')})

    )

    add_fieldsets = (
        (None,
         {'classes': ('wide',),
          'fields': ('email', 'username', 'first_name', 'last_name', 'phone_number','password1', 'password2')
          }

         ),
    )


admin.site.register(User, AccountAdminConfig)
