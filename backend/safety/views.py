
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import UserBlock, UserReport, SafetyIncident
from .serializers import (
    UserBlockSerializer,
    UserReportSerializer,
    SafetyIncidentSerializer,
)


class BlockUserView(generics.CreateAPIView):

    serializer_class = UserBlockSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(blocker=self.request.user)


class MyBlockedUsersView(generics.ListAPIView):

    serializer_class = UserBlockSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return UserBlock.objects.filter(blocker=self.request.user)


class ReportUserView(generics.CreateAPIView):

    serializer_class = UserReportSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(reporter=self.request.user)


class MyReportsView(generics.ListAPIView):

    serializer_class = UserReportSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return UserReport.objects.filter(reporter=self.request.user)


class CreateSafetyIncidentView(generics.CreateAPIView):

    serializer_class = SafetyIncidentSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(reported_by=self.request.user)


class MySafetyIncidentsView(generics.ListAPIView):

    serializer_class = SafetyIncidentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return SafetyIncident.objects.filter(
            reported_by=self.request.user
        )
