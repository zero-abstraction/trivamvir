
from django.urls import path
from .views import MyVerificationView

urlpatterns = [
    path('me/', MyVerificationView.as_view(), name='my-verification'),
]
