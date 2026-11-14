from rest_framework import serializers
from django.utils import timezone
from decimal import Decimal

from .models import Booking


class BookingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Booking

        fields = [
            'id',
            'venue',
            'player',
            'booking_date',
            'start_time',
            'end_time',
            'number_of_courts',
            'total_price',
            'status',
            'notes',
            'created_at',
            'updated_at',
        ]

        read_only_fields = [
            'id',
            'player',
            'total_price',
            'status',
            'created_at',
            'updated_at',
        ]

    def validate(self, data):

        venue = data.get(
            'venue',
            getattr(self.instance, 'venue', None)
        )

        booking_date = data.get(
            'booking_date',
            getattr(self.instance, 'booking_date', None)
        )

        start_time = data.get(
            'start_time',
            getattr(self.instance, 'start_time', None)
        )

        end_time = data.get(
            'end_time',
            getattr(self.instance, 'end_time', None)
        )

        number_of_courts = data.get(
            'number_of_courts',
            getattr(self.instance, 'number_of_courts', 1)
        )

        if venue and (
            not venue.is_approved
            or not venue.is_listed
            or not venue.accepts_direct_bookings
        ):
            raise serializers.ValidationError(
                "This venue is not accepting direct bookings."
            )

        if start_time and end_time and end_time <= start_time:
            raise serializers.ValidationError(
                "End time must be later than start time."
            )

        if booking_date and booking_date < timezone.localdate():
            raise serializers.ValidationError(
                "Booking date cannot be in the past."
            )

        if booking_date and start_time:
            booking_datetime = timezone.make_aware(
                timezone.datetime.combine(booking_date, start_time)
            )

            if booking_datetime <= timezone.now():
                raise serializers.ValidationError(
                    "Booking must be scheduled for a future time."
                )

        if venue and start_time and end_time:

            if start_time < venue.opening_time or end_time > venue.closing_time:
                raise serializers.ValidationError(
                    "Booking time must be within venue operating hours."
                )

        if venue and number_of_courts:

            if number_of_courts > venue.number_of_courts:
                raise serializers.ValidationError(
                    "Requested courts exceed venue capacity."
                )

        return data

    def create(self, validated_data):

        venue = validated_data['venue']
        start_time = validated_data['start_time']
        end_time = validated_data['end_time']
        number_of_courts = validated_data['number_of_courts']

        duration = (
            Decimal(
                (
                    end_time.hour * 60 + end_time.minute
                ) - (
                    start_time.hour * 60 + start_time.minute
                )
            ) / Decimal('60')
        )

        validated_data['total_price'] = (
            venue.price_per_hour * duration * number_of_courts
        )

        return super().create(validated_data)