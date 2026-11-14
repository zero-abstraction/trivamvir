
from rest_framework import serializers
from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile

        fields = [
            'id',
            'user',
            'full_name',
            'profile_picture',
            'bio',
            'date_of_birth',
            'city',
            'preferred_sports',
            'skill_level',
            'is_profile_public',
            'created_at',
            'updated_at',
        ]

        read_only_fields = [
            'id',
            'user',
            'created_at',
            'updated_at',
        ]
