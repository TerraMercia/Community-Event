from django.db import models
from django.utils import timezone

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField
    location = models.CharField(max_length=255)
    event_datetime = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["event_datetime"]

    def __str__(self):
        return f"{self.title} @ {self.location} ({self.event_datetime})"
# Create your models here.
