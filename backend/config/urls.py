"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
   path('api-auth/', include('rest_framework.urls')),

    path('api/users/', include('users.urls')),
    path('api/games/', include('games.urls')),
    path('api/venues/', include('venues.urls')),
    path('api/sports/', include('sports.urls')),
    path('api/participation/', include('participation.urls')),
    path('api/verification/', include('verification.urls')),
    path('api/ratings/', include('ratings.urls')),
    path('api/notifications/', include('notifications.urls')),
    path('api/safety/', include('safety.urls')),
    path('api/organizers',include('organizers.urls')),
    path('api/subscriptions/', include('subscriptions.urls')),
    path('api/bookings/', include('bookings.urls')),
]