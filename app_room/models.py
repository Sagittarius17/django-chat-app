from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Room(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField()
    slug = models.SlugField(unique=True)
    
    def __str__(self):
        return self.name

import pytz
import datetime as dt
status_timezone = pytz.timezone('Etc/UTC')
class Message(models.Model):
    room = models.ForeignKey(Room, related_name='messages', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='user', on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(default=status_timezone.localize(dt.datetime.now()))
    
    class Meta:
        ordering = ['timestamp',]