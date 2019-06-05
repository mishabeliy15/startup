from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    channelid = models.CharField(max_length=128, unique=True, blank=True, null=True)