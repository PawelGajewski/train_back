from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = models.CharField(max_length=20, unique=True, default="usr")
    password = models.CharField(max_length=255)
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    isClient = models.BooleanField(default=True)
    birthDate = models.DateTimeField()
    sex = models.CharField(max_length=10)
    height = models.FloatField(default=0.00)
    activity = models.CharField(max_length=255)
    goal = models.CharField(max_length=255)


class Weight(models.Model):
    ownerID = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True, blank=True)
    weight = models.FloatField()

class Chest(models.Model):
    ownerID = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True, blank=True)
    length = models.FloatField()

class Biceps(models.Model):
    ownerID = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True, blank=True)
    length = models.FloatField()


class BenchPress(models.Model):
    ownerID = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True, blank=True)
    weight = models.FloatField()


class Squat(models.Model):
    ownerID = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True, blank=True)
    weight = models.FloatField()


class Deadlift(models.Model):
    ownerID = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True, blank=True)
    weight = models.FloatField()


