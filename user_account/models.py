from django.db import models
from django.contrib.auth.models import AbstractUser
from user_account.managers import UserManager

# Create your models here.
class User(AbstractUser):
    email = models.EmailField(max_length=255, unique=True)
    username = None
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email
