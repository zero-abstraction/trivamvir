from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import authenticate

from .models import User


class UserRegistrationSerializer(serializers.ModelSerializer):

    password = serializers.CharField(
        write_only=True,
        required=True,
        validators=[validate_password]
    )

    class Meta:
        model = User

        fields = [
            'id',
            'email',
            'username',
            'first_name',
            'last_name',
            'phone_number',
            'password'
        ]

    def create(self, validated_data):

        password = validated_data.pop('password')

        user = User.objects.create_user(
            password=password,
            **validated_data
        )

        return user

class UserLoginSerializer(serializers.Serializer):

    identifier = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):

        identifier = attrs.get('identifier')
        password = attrs.get('password')

        user = authenticate(
            request=self.context.get('request'),
            username=identifier,
            password=password
        )

        if not user:
            raise serializers.ValidationError(
                "Invalid email/mobile number or password."
            )

        if not user.is_active:
            raise serializers.ValidationError(
                "This account is inactive."
            )

        attrs['user'] = user

        return attrs


class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = User

        fields = [
            'id',
            'email',
            'username',
            'first_name',
            'last_name',
            'phone_number',
            'is_verified',
            'date_joined'
        ]

        read_only_fields = [
            'id',
            'email',
            'is_verified',
            'date_joined'
        ]