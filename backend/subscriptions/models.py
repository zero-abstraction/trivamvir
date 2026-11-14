
from django.db import models
from django.conf import settings


class Subscription(models.Model):

    PLAN_CHOICES = [
        ('monthly', 'Monthly'),
        ('yearly', 'Yearly'),
    ]

    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('active', 'Active'),
        ('expired', 'Expired'),
        ('cancelled', 'Cancelled'),
    ]

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='subscriptions'
    )

    plan = models.CharField(
        max_length=20,
        choices=PLAN_CHOICES
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pending'
    )

    start_date = models.DateTimeField(null=True, blank=True)

    end_date = models.DateTimeField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    @property
    def is_active(self):
        from django.utils import timezone

        now = timezone.now()

        return (
            self.status == 'active'
            and self.start_date is not None
            and self.end_date is not None
            and self.start_date <= now < self.end_date
        )

    def __str__(self):
        return f"{self.user} - {self.plan} ({self.status})"
