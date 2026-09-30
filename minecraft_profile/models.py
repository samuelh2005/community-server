from django.db import models
from simple_history.models import HistoricalRecords

# Create your models here.

class MinecraftProfile(models.Model):
    history = HistoricalRecords()

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

class ProfileOwner(models.Model):
    history = HistoricalRecords()
    profile = models.ForeignKey(MinecraftProfile, on_delete=models.CASCADE)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    # Only one owner per profile, but a user can own multiple profiles (e.g. Java and Bedrock)
    class Meta:
        unique_together = ('profile', 'user')

    def __str__(self):
        return f"{self.user.username} owns {self.profile.username}"
