from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Call(models.Model):
    caller = models.ForeignKey(User, related_name="caller", on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name="receiver", on_delete=models.CASCADE)
    # You can also add fields like 'call_started_at', 'call_ended_at', etc.
