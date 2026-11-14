
from django.db import models
from django.conf import settings


class Venue(models.Model):

    # Ownership
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='owned_venues'
    )

    # Basic information
    name = models.CharField(max_length=150)
    address = models.TextField()
    contact_number = models.CharField(max_length=15)
    description = models.TextField(blank=True)

    # Location
    latitude = models.DecimalField(
        max_digits=9,
        decimal_places=6,
        null=True,
        blank=True
    )

    longitude = models.DecimalField(
        max_digits=9,
        decimal_places=6,
        null=True,
        blank=True
    )

    # Facilities
    number_of_courts = models.PositiveIntegerField(default=1)
    sports_offered = models.JSONField(default=list)

    # Operating hours
    opening_time = models.TimeField()
    closing_time = models.TimeField()

    # Pricing
    price_per_hour = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        default=0
    )

    # Visibility and bookings
    is_listed = models.BooleanField(default=False)
    accepts_direct_bookings = models.BooleanField(default=False)

    # Platform approval
    is_approved = models.BooleanField(default=False)

    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
