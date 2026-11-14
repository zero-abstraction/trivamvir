
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import Subscription
from .serializers import SubscriptionSerializer


class MySubscriptionsView(generics.ListAPIView):

    serializer_class = SubscriptionSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Subscription.objects.filter(
            user=self.request.user
        ).order_by('-created_at')


class CurrentSubscriptionView(generics.ListAPIView):

    serializer_class = SubscriptionSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        from django.utils import timezone

        now = timezone.now()

        return Subscription.objects.filter(
            user=self.request.user,
            status='active',
            start_date__lte=now,
            end_date__gt=now
        ).order_by('-created_at')[:1]
