
from django.urls import path

from .views import (
    NotificationListView,
    UnreadNotificationListView,
    MarkNotificationReadView,
)

urlpatterns = [
    path('', NotificationListView.as_view(), name='notification-list'),
    path('unread/', UnreadNotificationListView.as_view(), name='unread-notifications'),
    path('<int:pk>/read/', MarkNotificationReadView.as_view(), name='mark-notification-read'),
]
