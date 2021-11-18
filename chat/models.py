from django.db import models
from datetime import datetime


class Room(models.Model):
    room = models.CharField(max_length=100)

    def __str__(self):
        return self.room


class Messages(models.Model):
    date = models.DateTimeField(default=datetime.now, blank=True)
    value = models.CharField(max_length=100, default='0000000')
    user = models.CharField(max_length=100, default='0000000')
    room = models.CharField(max_length=100, default='0000000')