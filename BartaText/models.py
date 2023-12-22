from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=100)
    number = models.CharField(max_length=15, unique=True)
    profile_pic = models.ImageField(upload_to='profile_pics/', null=True, blank=True)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name

class Message(models.Model):
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return f"{self.user.name} - {self.timestamp}"
