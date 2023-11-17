from django.db import models

# Create your models here.
class Drama(models.Model):
    title = models.CharField(max_length=255)
    genre = models.CharField(max_length=200)
    director = models.CharField(max_length=200)
    writer = models.CharField(max_length=255)
    language= models.CharField(max_length=255)
    country = models.CharField(max_length=50)