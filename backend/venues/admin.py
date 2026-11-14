
from django.contrib import admin
from .models import Venue


@admin.register(Venue)
class VenueAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'owner',
        'contact_number',
        'is_approved',
        'is_listed',
    )

    list_filter = ('is_approved', 'is_listed')
    search_fields = ('name', 'address', 'contact_number')
