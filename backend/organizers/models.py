
from django.db import models
from django.conf import settings


class OrganizerProfile(models.Model):

    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
        ('suspended', 'Suspended'),
    ]

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='organizer_profile'
    )

    organization_name = models.CharField(max_length=150)

    description = models.TextField(blank=True)

    contact_email = models.EmailField(blank=True)

    contact_number = models.CharField(max_length=15, blank=True)

    website = models.URLField(blank=True)

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pending'
    )

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.organization_name
