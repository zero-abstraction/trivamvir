
from django.urls import path

from .views import (
    SubmitRatingView,
    MyReceivedRatingsView,
    MyGivenRatingsView,
)

urlpatterns = [
    path('submit/', SubmitRatingView.as_view(), name='submit-rating'),
    path('received/', MyReceivedRatingsView.as_view(), name='received-ratings'),
    path('given/', MyGivenRatingsView.as_view(), name='given-ratings'),
]
