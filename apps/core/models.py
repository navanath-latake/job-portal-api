from django.db import models
import uuid

class BaseModel(models.Model):
    """
    Abstract base — all models inherit from this.
    Every table automatically gets: UUID id, created_at, updated_at.
    """
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True