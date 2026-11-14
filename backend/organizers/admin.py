
from django.contrib import admin
from .models import OrganizerProfile


@admin.register(OrganizerProfile)
class OrganizerProfileAdmin(admin.ModelAdmin):

    list_display = (
        'organization_name',
        'user',
        'status',
        'created_at',
    )

    list_filter = ('status',)

    search_fields = (
        'organization_name',
        'user__email',
        'contact_email',
    )
