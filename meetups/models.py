from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# location models
class Location(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} {self.address}"
class Meetup(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)
    description = models.TextField(max_length=500)
    image = models.ImageField(upload_to="images",default ="default.png")
     
    def __str__(self):
        return f"{self.title} - ({self.slug})"