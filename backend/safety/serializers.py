
from rest_framework import serializers
from .models import UserBlock, UserReport, SafetyIncident


class UserBlockSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserBlock
        fields = ['id', 'blocker', 'blocked', 'created_at']
        read_only_fields = ['id', 'blocker', 'created_at']

    def validate_blocked(self, value):
        if value == self.context['request'].user:
            raise serializers.ValidationError(
                "You cannot block yourself."
            )
        return value


class UserReportSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserReport
        fields = [
            'id', 'reporter', 'reported_user',
            'reason', 'description', 'status', 'created_at'
        ]
        read_only_fields = ['id', 'reporter', 'status', 'created_at']

    def validate_reported_user(self, value):
        if value == self.context['request'].user:
            raise serializers.ValidationError(
                "You cannot report yourself."
            )
        return value


class SafetyIncidentSerializer(serializers.ModelSerializer):

    class Meta:
        model = SafetyIncident
        fields = [
            'id', 'reported_by', 'game', 'incident_type',
            'description', 'status', 'created_at', 'resolved_at'
        ]
        read_only_fields = [
            'id', 'reported_by', 'status', 'created_at', 'resolved_at'
        ]
