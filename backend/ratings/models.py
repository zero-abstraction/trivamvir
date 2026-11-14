
from django.db import models
from django.conf import settings


class PlayerRating(models.Model):

    game = models.ForeignKey(
        'games.Game',
        on_delete=models.CASCADE,
        related_name='player_ratings'
    )

    reviewer = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='ratings_given'
    )

    reviewed_player = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='ratings_received'
    )

    rating = models.PositiveSmallIntegerField(
        choices=[
            (1, 'Very Poor'),
            (2, 'Poor'),
            (3, 'Average'),
            (4, 'Good'),
            (5, 'Excellent'),
        ]
    )

    comment = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = (
            'game',
            'reviewer',
            'reviewed_player',
        )

    def __str__(self):
        return f"{self.reviewer} rated {self.reviewed_player}: {self.rating}"
