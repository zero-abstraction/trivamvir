
from django.db import models
from django.conf import settings


class Notification(models.Model):

    NOTIFICATION_TYPES = [
        ('game_joined', 'Game Joined'),
        ('game_cancelled', 'Game Cancelled'),
        ('waitlist_promoted', 'Waitlist Promoted'),
        ('game_reminder', 'Game Reminder'),
        ('game_updated', 'Game Updated'),
        ('new_message', 'New Message'),
        ('rating_received', 'Rating Received'),
        ('verification_update', 'Verification Update'),
        ('booking_update', 'Booking Update'),
        ('system', 'System Notification'),
    ]

    recipient = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='notifications'
    )

    title = models.CharField(max_length=150)

    message = models.TextField()

    notification_type = models.CharField(
        max_length=30,
        choices=NOTIFICATION_TYPES,
        default='system'
    )

    related_game = models.ForeignKey(
        'games.Game',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='notifications'
    )

    is_read = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.recipient} - {self.title}"
