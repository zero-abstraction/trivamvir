
from django.db import transaction
from django.db.models import Q
from django.shortcuts import get_object_or_404

from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from games.models import Game
from .models import GameParticipation
from .serializers import GameParticipationSerializer


class MyParticipationsView(generics.ListAPIView):

    serializer_class = GameParticipationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return GameParticipation.objects.filter(
            player=self.request.user
        ).select_related('game')


class JoinGameView(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request, game_id):

        with transaction.atomic():

            game = get_object_or_404(
                Game.objects.select_for_update(),
                pk=game_id
            )

            if game.host_id == request.user.id:
                return Response(
                    {"error": "You are already the host of this game."},
                    status=status.HTTP_400_BAD_REQUEST
                )

            if game.status != 'open':
                return Response(
                    {"error": "This game is not open for joining."},
                    status=status.HTTP_400_BAD_REQUEST
                )

            participation = GameParticipation.objects.filter(
                game=game,
                player=request.user
            ).first()

            if participation and participation.status != 'cancelled':
                return Response(
                    {"error": "You have already joined or waitlisted for this game."},
                    status=status.HTTP_400_BAD_REQUEST
                )

            confirmed_count = GameParticipation.objects.filter(
                game=game,
                status='confirmed'
            ).count()

            # The host occupies one player slot.
            total_players = confirmed_count + 1

            if total_players < game.max_players:
                new_status = 'confirmed'
            else:
                new_status = 'waitlisted'

            if participation:
                participation.status = new_status
                participation.save()
            else:
                participation = GameParticipation.objects.create(
                    game=game,
                    player=request.user,
                    status=new_status
                )

        return Response(
            GameParticipationSerializer(participation).data,
            status=status.HTTP_201_CREATED
        )


class LeaveGameView(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request, game_id):

        with transaction.atomic():

            game = get_object_or_404(
                Game.objects.select_for_update(),
                pk=game_id
            )

            participation = get_object_or_404(
                GameParticipation,
                game=game,
                player=request.user,
                status__in=['confirmed', 'waitlisted']
            )

            was_confirmed = participation.status == 'confirmed'

            participation.status = 'cancelled'
            participation.save()

            promoted_player = None

            if was_confirmed:

                promoted_player = (
                    GameParticipation.objects
                    .filter(game=game, status='waitlisted')
                    .order_by('joined_at')
                    .first()
                )

                if promoted_player:
                    promoted_player.status = 'confirmed'
                    promoted_player.save()

        return Response({
            "message": "You have left the game.",
            "promoted_player_id": (
                promoted_player.player_id if promoted_player else None
            )
        })


