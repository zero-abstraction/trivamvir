from django.urls import path
from . import views

urlpatterns = [
    path('', views.my_view, name='my_view'),
    path("api/", views.api_status, name="api_status"),
]