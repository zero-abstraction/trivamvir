
from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator


class Game(models.Model):

    SPORT_CHOICES = [
        ('badminton', 'Badminton'),
        ('football', 'Football'),
        ('cricket', 'Cricket'),
        ('basketball', 'Basketball'),
        ('tennis', 'Tennis'),
        ('volleyball', 'Volleyball'),
        ('table_tennis', 'Table Tennis'),
        ('running', 'Running'),
        ('other', 'Other'),
    ]

    SKILL_LEVEL_CHOICES = [
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
        ('any', 'Any Level'),
    ]

    STATUS_CHOICES = [
        ('open', 'Open'),
        ('cancelled', 'Cancelled'),
        ('completed', 'Completed'),
    ]

    # Game host
    host = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='hosted_games'
    )

    # Basic game information
    title = models.CharField(max_length=120)

    sport = models.CharField(
        max_length=30,
        choices=SPORT_CHOICES
    )

    description = models.TextField(blank=True)

    # Venue information
    venue_name = models.CharField(max_length=150)
    address = models.TextField()

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

    # Scheduling
    date_time = models.DateTimeField()

    # Participation requirements
    max_players = models.PositiveSmallIntegerField(
        default=4,
        validators=[
            MinValueValidator(2),
            MaxValueValidator(100)
        ]
    )

    skill_level = models.CharField(
        max_length=20,
        choices=SKILL_LEVEL_CHOICES,
        default='any'
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='open'
    )

    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} - {self.sport}"

    class Meta:
        ordering = ['date_time']
        verbose_name = 'Game'
        verbose_name_plural = 'Games'
