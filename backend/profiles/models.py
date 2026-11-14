
from django.db import models
from django.conf import settings


class Profile(models.Model):

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='profile'
    )

    full_name = models.CharField(max_length=150, blank=True)

    profile_picture = models.URLField(blank=True)

    bio = models.TextField(blank=True)

    date_of_birth = models.DateField(null=True, blank=True)

    city = models.CharField(max_length=100, blank=True)

    preferred_sports = models.ManyToManyField(
        'sports.Sport',
        blank=True,
        related_name='interested_players'
    )

    skill_level = models.CharField(
        max_length=20,
        choices=[
            ('beginner', 'Beginner'),
            ('intermediate', 'Intermediate'),
            ('advanced', 'Advanced'),
        ],
        blank=True
    )

    is_profile_public = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.full_name or self.user} Profile"
