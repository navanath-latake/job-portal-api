from django.db import models
from apps.core.models  import BaseModel
from django.conf import settings

class Application(BaseModel):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('under_review', 'Under Review'),
        ('interview', 'Interview'),
        ('offer', 'Offer'),
        ('rejected', 'Rejected')
    ]
    
    applicant = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete = models.CASCADE,
        related_name = 'applications',
        limit_choices_to = {'role':'applicant'},
        
    )
    
    job = models.ForeignKey(
        'jobs.job',
        on_delete=models.CASCADE,
        related_name='applications',
    )
    
    status = models.CharField(max_length=20, choices=STATUS_CHOICES,default='pending')
    cover_letter = models.TextField(blank=True)
    resume = models.FileField(upload_to='resumes/', blank=True, null=True)
    
    class Meta:
        ordering = ['-created_at']
        unique_together = ('applicant', 'job')
        
    def __str__(self):
        return f"{self.applicant.email} → {self.job.title} [{self.status}]"  