
from django.db import models
from django.conf import settings


class UserBlock(models.Model):

    blocker = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='blocked_users'
    )

    blocked = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='blocked_by_users'
    )

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('blocker', 'blocked')

    def __str__(self):
        return f"{self.blocker} blocked {self.blocked}"



class UserReport(models.Model):

    REASON_CHOICES = [
        ('harassment', 'Harassment'),
        ('abuse', 'Abusive Behaviour'),
        ('fake_profile', 'Fake Profile'),
        ('unsafe_behaviour', 'Unsafe Behaviour'),
        ('spam', 'Spam'),
        ('other', 'Other'),
    ]

    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('reviewing', 'Under Review'),
        ('resolved', 'Resolved'),
        ('dismissed', 'Dismissed'),
    ]

    reporter = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='reports_submitted'
    )

    reported_user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='reports_received'
    )

    reason = models.CharField(max_length=30, choices=REASON_CHOICES)

    description = models.TextField(blank=True)

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pending'
    )

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Report by {self.reporter} against {self.reported_user}"




class SafetyIncident(models.Model):

    INCIDENT_TYPES = [
        ('sos', 'SOS Alert'),
        ('venue_issue', 'Venue Safety Issue'),
        ('player_issue', 'Player Safety Issue'),
        ('other', 'Other'),
    ]

    STATUS_CHOICES = [
        ('open', 'Open'),
        ('investigating', 'Investigating'),
        ('resolved', 'Resolved'),
    ]

    reported_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='safety_incidents'
    )

    game = models.ForeignKey(
        'games.Game',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='safety_incidents'
    )

    incident_type = models.CharField(
        max_length=30,
        choices=INCIDENT_TYPES
    )

    description = models.TextField(blank=True)

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='open'
    )

    created_at = models.DateTimeField(auto_now_add=True)

    resolved_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.incident_type} - {self.reported_by}"
