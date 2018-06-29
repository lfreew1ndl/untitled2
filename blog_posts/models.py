from __future__ import unicode_literals
from django.db import models
from django.utils import timezone


# Create your models here.
class MyUser(models.Model):
    name = models.CharField(max_length=25)
    type = models.CharField(max_length=25)
    balance = models.FloatField()
    lastRequest = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name
