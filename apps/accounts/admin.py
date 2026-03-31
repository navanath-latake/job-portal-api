from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

# Register your models here.



from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display  = ['email', 'first_name', 'last_name', 'role', 'is_active', 'created_at']
    list_filter   = ['role', 'is_active', 'is_staff']
    search_fields = ['email', 'first_name', 'last_name']
    ordering      = ['-created_at']

    fieldsets = (
        (None,           {'fields': ('email', 'password')}),
        ('Personal Info',{'fields': ('first_name', 'last_name')}),
        ('Role & Access',{'fields': ('role', 'is_active', 'is_staff', 'is_superuser')}),
        ('Permissions',  {'fields': ('groups', 'user_permissions')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'last_name', 'role', 'password1', 'password2'),
        }),
    )