
from django.contrib import admin
from .models import UserBlock, UserReport, SafetyIncident


@admin.register(UserBlock)
class UserBlockAdmin(admin.ModelAdmin):
    list_display = ('blocker', 'blocked', 'created_at')
    search_fields = ('blocker__email', 'blocked__email')


@admin.register(UserReport)
class UserReportAdmin(admin.ModelAdmin):
    list_display = ('reporter', 'reported_user', 'reason', 'status')
    list_filter = ('reason', 'status')
    search_fields = ('reporter__email', 'reported_user__email')


@admin.register(SafetyIncident)
class SafetyIncidentAdmin(admin.ModelAdmin):
    list_display = ('reported_by', 'incident_type', 'status', 'created_at')
    list_filter = ('incident_type', 'status')
