from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from djongo import models
from octofit_tracker import models as octo_models

from django.db import connection

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        User = get_user_model()
        # Borrar datos existentes
        User.objects.all().delete()
        Team = octo_models.Team
        Activity = octo_models.Activity
        Leaderboard = octo_models.Leaderboard
        Workout = octo_models.Workout
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Crear equipos
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Crear usuarios
        tony = User.objects.create_user(username='tony', email='tony@marvel.com', password='ironman', team_name=marvel.name)
        steve = User.objects.create_user(username='steve', email='steve@marvel.com', password='cap', team_name=marvel.name)
        bruce = User.objects.create_user(username='bruce', email='bruce@dc.com', password='batman', team_name=dc.name)
        clark = User.objects.create_user(username='clark', email='clark@dc.com', password='superman', team_name=dc.name)

        # Crear actividades
        Activity.objects.create(user_email=tony.email, type='run', duration=30, calories=300)
        Activity.objects.create(user_email=steve.email, type='cycle', duration=45, calories=400)
        Activity.objects.create(user_email=bruce.email, type='swim', duration=60, calories=500)
        Activity.objects.create(user_email=clark.email, type='run', duration=50, calories=450)

        # Crear workouts
        Workout.objects.create(name='Full Body', description='Entrenamiento completo', duration=60)
        Workout.objects.create(name='Cardio Blast', description='Solo cardio', duration=30)

        # Crear leaderboard
        Leaderboard.objects.create(user_email=tony.email, score=1000)
        Leaderboard.objects.create(user_email=steve.email, score=900)
        Leaderboard.objects.create(user_email=bruce.email, score=950)
        Leaderboard.objects.create(user_email=clark.email, score=1100)

        self.stdout.write(self.style.SUCCESS('octofit_db poblada con datos de prueba'))
