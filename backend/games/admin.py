
from django.contrib import admin
from .models import Game


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):

    list_display = (
        'title',
        'sport',
        'host',
        'date_time',
        'max_players',
        'skill_level',
        'status',
    )

    list_filter = (
        'sport',
        'skill_level',
        'status',
    )

    search_fields = (
        'title',
        'venue_name',
        'address',
        'host__email',
    )

    ordering = ('date_time',)
