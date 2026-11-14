from django.urls import path

from .views import (
    MyBookingsView,
    VenueBookingsView,
    ManageBookingView,
    CancelBookingView,
)

urlpatterns = [

    path(
        'my/',
        MyBookingsView.as_view(),
        name='my-bookings'
    ),

    path(
        'venue/',
        VenueBookingsView.as_view(),
        name='venue-bookings'
    ),

    path(
        '<int:pk>/manage/',
        ManageBookingView.as_view(),
        name='manage-booking'
    ),

    path(
        '<int:pk>/cancel/',
        CancelBookingView.as_view(),
        name='cancel-booking'
    ),

]