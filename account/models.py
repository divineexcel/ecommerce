from django.contrib.auth.models import AbstractUser
from django.db import models


class UserTypes(models.TextChoices):
    ordinary_user = "Ordinary User"
    internal_user = "Internal User"


class User(AbstractUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=25, unique=True)
    first_name = models.CharField(max_length=100, unique=True)
    last_name = models.CharField(max_length=100, unique=True)
    user_type = models.CharField(max_length=100, choices=UserTypes.choices, default=UserTypes.ordinary_user)

    def __str__(self):
        return self.username
