from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Booking
from .serializers import BookingSerializer


class MyBookingsView(generics.ListCreateAPIView):

    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Booking.objects.filter(
            player=self.request.user
        ).select_related('venue')

    def perform_create(self, serializer):
        serializer.save(player=self.request.user)


class VenueBookingsView(generics.ListAPIView):

    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Booking.objects.filter(
            venue__owner=self.request.user
        ).select_related('venue', 'player')


class ManageBookingView(APIView):

    permission_classes = [IsAuthenticated]

    def patch(self, request, pk):

        try:
            booking = Booking.objects.get(
                pk=pk,
                venue__owner=request.user
            )

        except Booking.DoesNotExist:
            return Response(
                {"error": "Booking not found."},
                status=status.HTTP_404_NOT_FOUND
            )

        new_status = request.data.get('status')

        if new_status not in ['confirmed', 'rejected']:
            return Response(
                {"error": "Status must be confirmed or rejected."},
                status=status.HTTP_400_BAD_REQUEST
            )

        if booking.status != 'pending':
            return Response(
                {"error": "Only pending bookings can be managed."},
                status=status.HTTP_400_BAD_REQUEST
            )

        booking.status = new_status
        booking.save()

        return Response(BookingSerializer(booking).data)


class CancelBookingView(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request, pk):

        try:
            booking = Booking.objects.get(
                pk=pk,
                player=request.user
            )

        except Booking.DoesNotExist:
            return Response(
                {"error": "Booking not found."},
                status=status.HTTP_404_NOT_FOUND
            )

        if booking.status not in ['pending', 'confirmed']:
            return Response(
                {"error": "This booking cannot be cancelled."},
                status=status.HTTP_400_BAD_REQUEST
            )

        booking.status = 'cancelled'
        booking.save()

        return Response({
            "message": "Booking cancelled successfully."
        })