from django.db import models


class Language(models.Model):
    display = models.CharField(max_length=32)
    code = models.CharField(max_length=6, unique=True)
