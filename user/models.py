from django.db import models
from django.contrib.auth.models import User, AbstractUser
# Create your models here.


class UserTypes(models.TextChoices):
    ordinary_user = "Ordinary User"
    internal_user = "Internal User"
    


class User(AbstractUser):
    email= models.EmailField(unique=True)
    username= models.CharField(max_length=25, unique=True)
    first_name = models.CharField(max_length=100, unique=True)
    last_name = models.CharField(max_length=100, unique=True)
    user_type = models.CharField(max_length=100, choices=UserTypes.choices, default=UserTypes.ordinary_user)
    

    # USERNAME_FIELD= "email"
    # REQUIERED_FIELD=['email']
    def __str__(self):
        return self.username
