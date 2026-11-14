
from django.contrib import admin
from .models import UserVerification


@admin.register(UserVerification)
class UserVerificationAdmin(admin.ModelAdmin):

    list_display = (
        'user',
        'is_phone_verified',
        'identity_status',
        'verified_at',
    )

    list_filter = (
        'is_phone_verified',
        'identity_status',
    )

    search_fields = ('user__email', 'phone_number')
