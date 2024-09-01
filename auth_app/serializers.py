from rest_framework import serializers
from auth_app.services import create_user, user_by_email


class UserSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150, required=False, allow_null=True)
    email = serializers.EmailField()
    is_active = serializers.BooleanField(required=False, allow_null=True)


class UserCreateSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150, required=False, allow_null=True)
    email = serializers.EmailField()

    def create(self, validated_data):
        user = user_by_email(email=validated_data.get("email"))
        if user:
            return user
        user = create_user(
            email=validated_data.get("email"), username=validated_data.get("username")
        )
        return user


class UsernameSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150)


class EmailSerializer(serializers.Serializer):
    email = serializers.EmailField()
