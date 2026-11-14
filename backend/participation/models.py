
from django.db import models
from django.conf import settings


class GameParticipation(models.Model):

    STATUS_CHOICES = [
        ('confirmed', 'Confirmed'),
        ('waitlisted', 'Waitlisted'),
        ('cancelled', 'Cancelled'),
    ]

    game = models.ForeignKey(
        'games.Game',
        on_delete=models.CASCADE,
        related_name='participations'
    )

    player = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='game_participations'
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='confirmed'
    )

    joined_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('game', 'player')
        ordering = ['joined_at']

    def __str__(self):
        return f"{self.player} - {self.game} ({self.status})"
