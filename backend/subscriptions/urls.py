
from django.urls import path

from .views import (
    MySubscriptionsView,
    CurrentSubscriptionView,
)

urlpatterns = [
    path('', MySubscriptionsView.as_view(), name='my-subscriptions'),
    path('current/', CurrentSubscriptionView.as_view(), name='current-subscription'),
]
