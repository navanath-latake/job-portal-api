from django.contrib import admin
from .models import Job


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display  = ['title', 'company', 'recruiter', 'work_type',
                     'experience_level', 'is_active', 'created_at']
    list_filter   = ['work_type', 'experience_level', 'is_active']
    search_fields = ['title', 'company', 'location']
    ordering      = ['-created_at']
    readonly_fields = ['created_at', 'updated_at']