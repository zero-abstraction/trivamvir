
from django.contrib import admin
from .models import GameParticipation


@admin.register(GameParticipation)
class GameParticipationAdmin(admin.ModelAdmin):

    list_display = ('player', 'game', 'status', 'joined_at')

    list_filter = ('status', 'joined_at')

    search_fields = ('player__email', 'game__title')
