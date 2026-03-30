from django.db import models
from django.contrib.postgres.indexes import GinIndex
from apps.core.models import BaseModel
from django.conf import settings

class Job(BaseModel):
    EXPERIENCE_CHOICES = [
        ('entry', 'Entry Level'),
        ('mid', 'Mid Level'),
        ('senior', 'Senior Level'),
        ('lead', 'Lead / principal'),
    ]
    
    WORK_TYPE_CHOICES = [
        ('remote', 'Remote'),
        ('onsite', 'On-site'),
        ('hybrid', 'Hybrid'),
    ]
    
    recruiter = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete = models.CASCADE,
        related_name = 'job_postings',
        limit_choices_to = {'role':'recruiter'},
    )
    
    title = models.CharField(max_length=200)
    description = models.TextField()
    company = models.CharField(max_length=150)
    location = models.CharField(max_length=150)
    work_type = models.CharField(max_length=10, choices=WORK_TYPE_CHOICES, default='onsite')
    experience_level = models.CharField(max_length=10, choices=EXPERIENCE_CHOICES, default='mid')
    salary_min = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    salary_max = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    skills_required = models.JSONField(default=list)
    is_active = models.BooleanField(default=True)
    deadline = models.DateField(null=True, blank=True)
    
    class Meta:
        ordering = ['-created_at']
        indexes = [
            GinIndex(fields=['skills_required'], name='job_skills_gin_idx'),
        ]
    
    def __str__(self):
        return f"{self.title} @ {self.company}" 
    
    def clean(self):
        from django.core.exceptions import ValidationError
        if self.salary_min and self.salary_max:
            if self.salary_min > self.salary_max:
                raise ValidationError("Salary_min cannot exceed salary_max.")  