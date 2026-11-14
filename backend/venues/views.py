
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, BasePermission

from .models import Venue
from .serializers import VenueSerializer


class IsOwnerOrReadOnly(BasePermission):
    """
    Only the venue owner can modify or delete a venue.
    Other users can view it if it is publicly available.
    """

    def has_object_permission(self, request, view, obj):

        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return True

        return obj.owner == request.user


class VenueListCreateView(generics.ListCreateAPIView):

    serializer_class = VenueSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return Venue.objects.filter(
            is_approved=True,
            is_listed=True
        )

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class VenueDetailView(generics.RetrieveUpdateDestroyAPIView):

    serializer_class = VenueSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def get_queryset(self):
        return Venue.objects.filter(
            is_approved=True,
            is_listed=True
        ) | Venue.objects.filter(owner=self.request.user)
