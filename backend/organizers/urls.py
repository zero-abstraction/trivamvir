
from django.urls import path

from .views import (
    OrganizerRegistrationView,
    MyOrganizerProfileView,
)

urlpatterns = [
    path('register/', OrganizerRegistrationView.as_view(), name='organizer-register'),
    path('me/', MyOrganizerProfileView.as_view(), name='my-organizer-profile'),
]
