from django.db import models
from django.conf import settings

class Application(models.Model):
    class Status(models.TextChoices):
        PENDING     = 'pending',     'Pending'
        REVIEWING   = 'reviewing',   'Under Review'
        SHORTLISTED = 'shortlisted', 'Shortlisted'
        OFFERED     = 'offered',     'Offer Extended'
        REJECTED    = 'rejected',    'Rejected'

    candidate    = models.ForeignKey(
                     settings.AUTH_USER_MODEL,
                     on_delete=models.CASCADE,
                     related_name='applications')
    job          = models.ForeignKey(
                     'jobs.Job',
                     on_delete=models.CASCADE,
                     related_name='applications')
    cover_letter = models.TextField(blank=True)
    resume       = models.FileField(
                     upload_to='resumes/', null=True, blank=True)
    status       = models.CharField(max_length=20,
                     choices=Status.choices,
                     default=Status.PENDING)
    created_at   = models.DateTimeField(auto_now_add=True)
    updated_at   = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = [('candidate', 'job')]
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.candidate.email} → {self.job.title}"