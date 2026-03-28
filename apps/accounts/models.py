
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    class Role(models.TextChoices):
        RECRUITER = 'recruiter', 'Recruiter'
        CANDIDATE = 'candidate', 'Candidate'

    email = models.EmailField(unique=True)
    role  = models.CharField(
                max_length=20,
                choices=Role.choices,
                default=Role.CANDIDATE)
    bio   = models.TextField(blank=True)
    phone = models.CharField(max_length=15, blank=True)

    USERNAME_FIELD  = 'email'
    REQUIRED_FIELDS = ['username']

    @property
    def is_recruiter(self):
        return self.role == self.Role.RECRUITER

    def __str__(self):
        return self.email