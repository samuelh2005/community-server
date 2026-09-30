from django.contrib import admin

from minecraft_profile.models import MinecraftProfile, ProfileOwner

# Register your models here.
admin.site.register(MinecraftProfile)
admin.site.register(ProfileOwner)