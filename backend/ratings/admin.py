
from django.contrib import admin
from .models import PlayerRating


@admin.register(PlayerRating)
class PlayerRatingAdmin(admin.ModelAdmin):

    list_display = (
        'game',
        'reviewer',
        'reviewed_player',
        'rating',
        'created_at',
    )

    list_filter = ('rating', 'created_at')

    search_fields = (
        'reviewer__email',
        'reviewed_player__email',
        'game__title',
    )
