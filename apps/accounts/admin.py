from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

# Register your models here.



@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display  = ['email', 'username', 'role', 'is_active', 'date_joined']
    list_filter   = ['role', 'is_active', 'is_staff']
    search_fields = ['email', 'username', 'first_name', 'last_name']
    ordering      = ['-date_joined']

    fieldsets = UserAdmin.fieldsets + (
        ('Role Info', {'fields': ('role',)}),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Role Info', {'fields': ('role',)}),
    )