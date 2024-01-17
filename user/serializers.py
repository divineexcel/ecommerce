from rest_framework import serializers
# from django.contrib.auth.models import User
from rongry.models import User


class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        pass
        model = User
        fields = ['username', 'email', 'password']