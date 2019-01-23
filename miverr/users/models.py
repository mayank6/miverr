from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager

class CustomUserManager(UserManager):
    pass

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    avatar=models.CharField(max_length=500)
    about=models.CharField(max_length=1000)
    slogan=models.CharField(max_length=100)
    def __str__(self):
        return self.username
    objects = CustomUserManager()
