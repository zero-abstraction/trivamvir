
from rest_framework import serializers
from .models import GameParticipation


class GameParticipationSerializer(serializers.ModelSerializer):

    class Meta:
        model = GameParticipation

        fields = [
            'id',
            'game',
            'player',
            'status',
            'joined_at',
            'updated_at',
        ]

        read_only_fields = [
            'id',
            'player',
            'status',
            'joined_at',
            'updated_at',
        ]
