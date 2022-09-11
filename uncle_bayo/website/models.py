from email.mime import image
from django.db import models


# Create your models here.


class Work(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    image = models.ImageField(upload_to='uploads/')
    summary = models.TextField()
    areas = models.TextField()


class Team(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    position = models.CharField(max_length=20)
    image = models.ImageField(upload_to='uploads/')
