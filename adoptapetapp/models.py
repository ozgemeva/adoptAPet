from django.db import models
from django.contrib.auth.models import User

class Person(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    zipnum = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=30)
    email = models.CharField(max_length=30)

class Pet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=0)
    name = models.CharField(max_length=50)
    variety = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    age = models.CharField(max_length=50)
    address = models.CharField(max_length=300)
    weight = models.CharField(max_length=50)
    description = models.CharField(max_length=55)
    photo = models.FileField()
class Comment(models.Model):
    commenter = models.ForeignKey(User, on_delete=models.CASCADE, default=0)
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE, default=0)
    comment = models.CharField(max_length = 150)
