
from rest_framework import serializers
from .models import UserVerification


class UserVerificationSerializer(serializers.ModelSerializer):

    is_verified = serializers.ReadOnlyField()

    class Meta:
        model = UserVerification

        fields = [
            'id',
            'phone_number',
            'is_phone_verified',
            'identity_status',
            'identity_document_submitted',
            'selfie_submitted',
            'is_verified',
            'verified_at',
            'created_at',
        ]

        read_only_fields = [
            'id',
            'is_phone_verified',
            'identity_status',
            'identity_document_submitted',
            'selfie_submitted',
            'is_verified',
            'verified_at',
            'created_at',
        ]
