from django.db import models
from django.conf import settings


class Booking(models.Model):

    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('rejected', 'Rejected'),
        ('cancelled', 'Cancelled'),
    ]

    venue = models.ForeignKey(
        'venues.Venue',
        on_delete=models.CASCADE,
        related_name='bookings'
    )

    player = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='venue_bookings'
    )

    booking_date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()

    number_of_courts = models.PositiveIntegerField(default=1)

    total_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pending'
    )

    notes = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.player} - {self.venue} ({self.booking_date})"