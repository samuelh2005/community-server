from django.db import models
from django.conf import settings
from simple_history.models import HistoricalRecords

# Create your models here.

class MinecraftProfile(models.Model):
    history = HistoricalRecords()
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='minecraft_profiles', null=True, blank=True)

    class MinecraftProfileType(models.TextChoices):
        JAVA = 'java', 'Java'
        BEDROCK = 'bedrock', 'Bedrock'

    type = models.CharField(max_length=10, choices=MinecraftProfileType.choices)

    # User names can be longer than 16 characters for Bedrock Edition.
    username = models.CharField(max_length=255, unique=True)

    # UUIDs are unique across both editions
    uuid = models.UUIDField(unique=True)

    # xbox_id is only available for Bedrock Edition
    xbox_id = models.CharField(max_length=255, unique=True, null=True, blank=True)
    xbox_gamertag = models.CharField(max_length=255, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username
