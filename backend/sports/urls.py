
from django.urls import path

from .views import (
    SportListView,
    SportDetailView,
    SportCreateView,
    SportUpdateView,
    SportDeleteView,
)

urlpatterns = [
    path('', SportListView.as_view(), name='sport-list'),
    path('create/', SportCreateView.as_view(), name='sport-create'),
    path('<int:pk>/', SportDetailView.as_view(), name='sport-detail'),
    path('<int:pk>/update/', SportUpdateView.as_view(), name='sport-update'),
    path('<int:pk>/delete/', SportDeleteView.as_view(), name='sport-delete'),
]
