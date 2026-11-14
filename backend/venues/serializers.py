
from rest_framework import serializers
from .models import Venue


class VenueSerializer(serializers.ModelSerializer):

    class Meta:
        model = Venue

        fields = [
            'id',
            'owner',
            'name',
            'address',
            'contact_number',
            'description',
            'latitude',
            'longitude',
            'number_of_courts',
            'sports_offered',
            'opening_time',
            'closing_time',
            'price_per_hour',
            'is_listed',
            'accepts_direct_bookings',
            'is_approved',
        ]

        read_only_fields = [
            'id',
            'owner',
            'is_approved',
        ]

    def validate(self, data):

        opening_time = data.get(
            'opening_time',
            getattr(self.instance, 'opening_time', None)
        )

        closing_time = data.get(
            'closing_time',
            getattr(self.instance, 'closing_time', None)
        )

        if opening_time and closing_time:
            if opening_time >= closing_time:
                raise serializers.ValidationError(
                    "Closing time must be later than opening time."
                )

        return data
