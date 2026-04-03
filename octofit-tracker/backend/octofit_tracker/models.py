from djongo import models
from django.contrib.auth.models import AbstractUser

class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)
    def __str__(self):
        return self.name

class User(AbstractUser):
    email = models.EmailField(unique=True)
    team_name = models.CharField(max_length=100, blank=True, null=True)  # Referencia por nombre

class Activity(models.Model):
    user_email = models.EmailField()  # Referencia por email
    type = models.CharField(max_length=50)
    duration = models.IntegerField()  # minutos
    calories = models.IntegerField()
    def __str__(self):
        return f"{self.user_email} - {self.type}"

class Workout(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    duration = models.IntegerField()  # minutos
    def __str__(self):
        return self.name

class Leaderboard(models.Model):
    user_email = models.EmailField()  # Referencia por email
    score = models.IntegerField()
    def __str__(self):
        return f"{self.user_email}: {self.score}"
