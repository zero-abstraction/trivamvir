
from rest_framework import serializers
from .models import PlayerRating


class PlayerRatingSerializer(serializers.ModelSerializer):

    class Meta:
        model = PlayerRating

        fields = [
            'id',
            'game',
            'reviewer',
            'reviewed_player',
            'rating',
            'comment',
            'created_at',
        ]

        read_only_fields = [
            'id',
            'reviewer',
            'created_at',
        ]
