from django.db import models
from django.contrib.auth.models import  AbstractUser


class User(AbstractUser):
    bio = models.TextField(null=True, blank=True)

    class Meta():
        swappable = 'AUTH_USER_MODEL'
        verbose_name = 'User'
        verbose_name_plural = 'Users'