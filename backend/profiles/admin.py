
from django.contrib import admin
from .models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):

    list_display = ('full_name', 'user', 'city', 'skill_level')

    list_filter = ('skill_level', 'is_profile_public')

    search_fields = ('full_name', 'city', 'user__email')
