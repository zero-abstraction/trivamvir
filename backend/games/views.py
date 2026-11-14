
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.exceptions import PermissionDenied
from django.utils import timezone

from .models import Game
from .serializers import GameSerializer


class GameListCreateView(generics.ListCreateAPIView):

    serializer_class = GameSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return Game.objects.filter(
            status='open',
            date_time__gte=timezone.now()
        ).select_related('host')

    def perform_create(self, serializer):
        serializer.save(host=self.request.user)


class GameDetailView(generics.RetrieveUpdateDestroyAPIView):

    serializer_class = GameSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return Game.objects.select_related('host').all()

    def perform_update(self, serializer):
        game = self.get_object()

        if game.host != self.request.user:
            raise PermissionDenied(
                "You can only edit games that you created."
            )

        serializer.save()

    def perform_destroy(self, instance):
        if instance.host != self.request.user:
            raise PermissionDenied(
                "You can only delete games that you created."
            )

        instance.delete()
