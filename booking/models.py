from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

class Booking(models.Model):
    id = models.IntegerField(primary_key=True)
    guests = models.IntegerField()
    date = models.DateField()
    time = models.TimeField()
    requirements = models.CharField(max_length=200)
    user = models.IntegerField()

class User(models.Model):
    id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=80)
    password = models.CharField(max_length=80)

class Profile(models.Model):
    id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    email = models.EmailField()
    requirements = models.CharField(max_length=200)
    user = models.IntegerField()
