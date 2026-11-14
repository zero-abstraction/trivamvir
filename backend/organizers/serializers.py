
from rest_framework import serializers
from .models import OrganizerProfile


class OrganizerProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrganizerProfile

        fields = [
            'id',
            'user',
            'organization_name',
            'description',
            'contact_email',
            'contact_number',
            'website',
            'status',
            'created_at',
            'updated_at',
        ]

        read_only_fields = [
            'id',
            'user',
            'status',
            'created_at',
            'updated_at',
        ]
