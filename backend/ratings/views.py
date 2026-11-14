
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import PlayerRating
from .serializers import PlayerRatingSerializer


class SubmitRatingView(generics.CreateAPIView):

    serializer_class = PlayerRatingSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(reviewer=self.request.user)


class MyReceivedRatingsView(generics.ListAPIView):

    serializer_class = PlayerRatingSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return PlayerRating.objects.filter(
            reviewed_player=self.request.user
        ).order_by('-created_at')


class MyGivenRatingsView(generics.ListAPIView):

    serializer_class = PlayerRatingSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return PlayerRating.objects.filter(
            reviewer=self.request.user
        ).order_by('-created_at')
