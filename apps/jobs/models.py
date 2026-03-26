from django.db import models

# Create your models here.
from django.db import models
from django.conf import settings

class Job(models.Model):
    class Status(models.TextChoices):
        DRAFT  = 'draft',  'Draft'
        ACTIVE = 'active', 'Active'
        CLOSED = 'closed', 'Closed'

    class JobType(models.TextChoices):
        FULL_TIME  = 'full_time',  'Full Time'
        PART_TIME  = 'part_time',  'Part Time'
        CONTRACT   = 'contract',   'Contract'
        REMOTE     = 'remote',     'Remote'
        INTERNSHIP = 'internship', 'Internship'

    recruiter   = models.ForeignKey(
                    settings.AUTH_USER_MODEL,
                    on_delete=models.CASCADE,
                    related_name='posted_jobs')
    title       = models.CharField(max_length=200)
    description = models.TextField()
    company     = models.CharField(max_length=150)
    location    = models.CharField(max_length=100)
    job_type    = models.CharField(max_length=20,
                    choices=JobType.choices,
                    default=JobType.FULL_TIME)
    salary_min  = models.DecimalField(
                    max_digits=10, decimal_places=2,
                    null=True, blank=True)
    salary_max  = models.DecimalField(
                    max_digits=10, decimal_places=2,
                    null=True, blank=True)
    skills      = models.JSONField(default=list, blank=True)
    status      = models.CharField(max_length=10,
                    choices=Status.choices,
                    default=Status.DRAFT)
    deadline    = models.DateField(null=True, blank=True)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.title} @ {self.company}"