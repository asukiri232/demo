from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('Персональные данные', {'fields': ('full_name', 'phone')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Персональные данные', {'fields': ('full_name', 'phone', 'email')}),
    )
    list_display = ('username', 'full_name', 'email', 'phone', 'is_staff')
    search_fields = ('username', 'full_name', 'email', 'phone')
