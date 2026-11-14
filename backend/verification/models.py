
from django.db import models
from django.conf import settings


class UserVerification(models.Model):

    STATUS_CHOICES = [
        ('not_started', 'Not Started'),
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='verification'
    )

    phone_number = models.CharField(max_length=15, blank=True)

    is_phone_verified = models.BooleanField(default=False)

    identity_status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='not_started'
    )

    identity_document_submitted = models.BooleanField(default=False)

    selfie_submitted = models.BooleanField(default=False)

    verified_at = models.DateTimeField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    @property
    def is_verified(self):
        return (
            self.is_phone_verified
            and self.identity_status == 'approved'
        )

    def __str__(self):
        return f"{self.user} Verification"
