
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import UserVerification
from .serializers import UserVerificationSerializer


class MyVerificationView(generics.RetrieveAPIView):

    serializer_class = UserVerificationSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        verification, created = UserVerification.objects.get_or_create(
            user=self.request.user
        )

        return verification
