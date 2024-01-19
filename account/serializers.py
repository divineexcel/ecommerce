from password_validator import PasswordValidator
from rest_framework import serializers
from rongry.models import User


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, attrs):
        username = attrs.get("username").lower()
        password = attrs.get("password")

        return {
            "username": username,
            "password": password
        }


class RegisterSerializer(serializers.Serializer):
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    email = serializers.EmailField()
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, attrs):
        data = attrs.copy()

        data["username"] = data.get("username").lower()
        password = data.get("password")

        password_validator = PasswordValidator()
        password_validator.min(8).uppercase().lowercase().digits().symbols()

        if not password_validator.validate(password):
            raise serializers.ValidationError("Password is too weak", "password")

        return data


class LoginResponseSerializer(serializers.Serializer):
    access_token = serializers.CharField()
    user_type = serializers.CharField()
    username = serializers.CharField()
    full_name = serializers.CharField()


class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        pass
        model = User
        fields = ['username', 'email', 'password']


class RegisterResponseSerializer(serializers.Serializer):
    message = serializers.CharField()
    email = serializers.CharField()


class LogoutSerializer(serializers.Serializer):
    refresh_token= serializers.CharField()
    


