
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import OrganizerProfile
from .serializers import OrganizerProfileSerializer


class OrganizerRegistrationView(generics.CreateAPIView):

    serializer_class = OrganizerProfileSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class MyOrganizerProfileView(generics.RetrieveUpdateAPIView):

    serializer_class = OrganizerProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return OrganizerProfile.objects.get(
            user=self.request.user
        )
