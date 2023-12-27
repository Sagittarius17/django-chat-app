from django.db import models

class Room(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField()
    slug = models.SlugField(unique=True)
    
    def __str__(self):
        return self.name
