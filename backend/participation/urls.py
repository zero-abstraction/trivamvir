
from django.urls import path

from .views import (
    MyParticipationsView,
    JoinGameView,
    LeaveGameView,
)

urlpatterns = [
    path('my/', MyParticipationsView.as_view(), name='my-participations'),
    path('<int:game_id>/join/', JoinGameView.as_view(), name='join-game'),
    path('<int:game_id>/leave/', LeaveGameView.as_view(), name='leave-game'),
]
