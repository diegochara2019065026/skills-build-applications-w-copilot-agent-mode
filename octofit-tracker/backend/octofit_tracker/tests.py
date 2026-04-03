from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class ModelSmokeTest(TestCase):
    def test_team_create(self):
        t = Team.objects.create(name='TestTeam')
        self.assertEqual(str(t), 'TestTeam')
    def test_user_create(self):
        u = User.objects.create_user(username='test', email='test@test.com', password='1234', team_name='TestTeam')
        self.assertEqual(u.email, 'test@test.com')
    def test_activity_create(self):
        a = Activity.objects.create(user_email='test@test.com', type='run', duration=10, calories=100)
        self.assertEqual(a.type, 'run')
    def test_workout_create(self):
        w = Workout.objects.create(name='W1', description='desc', duration=20)
        self.assertEqual(w.name, 'W1')
    def test_leaderboard_create(self):
        l = Leaderboard.objects.create(user_email='test@test.com', score=123)
        self.assertEqual(l.score, 123)
