
from django.urls import path

from .views import (
    BlockUserView,
    MyBlockedUsersView,
    ReportUserView,
    MyReportsView,
    CreateSafetyIncidentView,
    MySafetyIncidentsView,
)

urlpatterns = [
    path('block/', BlockUserView.as_view(), name='block-user'),
    path('blocked/', MyBlockedUsersView.as_view(), name='my-blocked-users'),
    path('report/', ReportUserView.as_view(), name='report-user'),
    path('reports/', MyReportsView.as_view(), name='my-reports'),
    path('incident/', CreateSafetyIncidentView.as_view(), name='create-incident'),
    path('incidents/', MySafetyIncidentsView.as_view(), name='my-incidents'),
]
