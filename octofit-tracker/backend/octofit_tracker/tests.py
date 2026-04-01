from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class ModelTests(TestCase):
    def test_team_creation(self):
        team = Team.objects.create(_id='test', name='Test Team')
        self.assertEqual(str(team), 'Test Team')

    def test_user_creation(self):
        team = Team.objects.create(_id='test', name='Test Team')
        user = User.objects.create(name='Test User', email='test@example.com', team=team)
        self.assertEqual(str(user), 'Test User')

    def test_activity_creation(self):
        team = Team.objects.create(_id='test', name='Test Team')
        user = User.objects.create(name='Test User', email='test@example.com', team=team)
        activity = Activity.objects.create(user=user, type='run', distance=5, duration=30)
        self.assertEqual(str(activity), 'Test User - run')

    def test_workout_creation(self):
        team = Team.objects.create(_id='test', name='Test Team')
        user = User.objects.create(name='Test User', email='test@example.com', team=team)
        workout = Workout.objects.create(user=user, workout='Pushups', reps=10)
        self.assertEqual(str(workout), 'Test User - Pushups')

    def test_leaderboard_creation(self):
        team = Team.objects.create(_id='test', name='Test Team')
        leaderboard = Leaderboard.objects.create(team=team, points=100)
        self.assertEqual(str(leaderboard), 'Test Team - 100')
