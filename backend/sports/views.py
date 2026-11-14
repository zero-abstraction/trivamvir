
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from .models import Sport
from .serializers import SportSerializer


class SportListView(generics.ListAPIView):

    serializer_class = SportSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Sport.objects.filter(is_active=True)


class SportDetailView(generics.RetrieveAPIView):

    serializer_class = SportSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Sport.objects.filter(is_active=True)


class SportCreateView(generics.CreateAPIView):

    queryset = Sport.objects.all()
    serializer_class = SportSerializer
    permission_classes = [IsAdminUser]


class SportUpdateView(generics.UpdateAPIView):

    queryset = Sport.objects.all()
    serializer_class = SportSerializer
    permission_classes = [IsAdminUser]


class SportDeleteView(generics.DestroyAPIView):

    queryset = Sport.objects.all()
    serializer_class = SportSerializer
    permission_classes = [IsAdminUser]
