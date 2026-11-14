
from rest_framework import serializers
from .models import Subscription


class SubscriptionSerializer(serializers.ModelSerializer):

    is_active = serializers.ReadOnlyField()

    class Meta:
        model = Subscription

        fields = [
            'id',
            'user',
            'plan',
            'status',
            'start_date',
            'end_date',
            'is_active',
            'created_at',
        ]

        read_only_fields = fields
