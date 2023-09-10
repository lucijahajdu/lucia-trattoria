from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Booking(models.Model):

    guests = models.PositiveIntegerField()
    date = models.DateField()
    time = models.TimeField()
    first_name = models.CharField(max_length=50, default='John')
    last_name = models.CharField(max_length=50, default='Adams')
    email = models.EmailField(default='example@email.com')
    requirements = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name


class Profile(models.Model):

    first_name = models.CharField(max_length=80, default='John')
    last_name = models.CharField(max_length=80, default='Adams')
    email = models.EmailField(default='example@email.com')
    requirements = models.CharField(max_length=200)
    user = models.OneToOneField(User, on_delete=models.CASCADE)