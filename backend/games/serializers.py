
from rest_framework import serializers
from django.utils import timezone
from .models import Game


class GameSerializer(serializers.ModelSerializer):

    class Meta:
        model = Game

        fields = [
            'id',
            'host',
            'title',
            'sport',
            'description',
            'venue_name',
            'address',
            'latitude',
            'longitude',
            'date_time',
            'max_players',
            'skill_level',
            'status',
            'created_at',
            'updated_at',
        ]

        read_only_fields = [
            'id',
            'host',
            'created_at',
            'updated_at',
        ]

    def validate_date_time(self, value):
        if value <= timezone.now():
            raise serializers.ValidationError(
                "Game date and time must be in the future."
            )

        return value
