from django.core.management.base import BaseCommand
from django.conf import settings
from pymongo import MongoClient

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        client = MongoClient('localhost', 27017)
        db = client['octofit_db']
        # Clear collections
        db.users.delete_many({})
        db.teams.delete_many({})
        db.activities.delete_many({})
        db.leaderboard.delete_many({})
        db.workouts.delete_many({})

        # Teams
        marvel = {'_id': 'marvel', 'name': 'Team Marvel'}
        dc = {'_id': 'dc', 'name': 'Team DC'}
        db.teams.insert_many([marvel, dc])

        # Users
        users = [
            {'name': 'Iron Man', 'email': 'ironman@marvel.com', 'team': 'marvel'},
            {'name': 'Captain America', 'email': 'cap@marvel.com', 'team': 'marvel'},
            {'name': 'Wonder Woman', 'email': 'wonderwoman@dc.com', 'team': 'dc'},
            {'name': 'Batman', 'email': 'batman@dc.com', 'team': 'dc'},
        ]
        db.users.insert_many(users)
        db.users.create_index('email', unique=True)

        # Activities
        activities = [
            {'user': 'ironman@marvel.com', 'type': 'run', 'distance': 5, 'duration': 30},
            {'user': 'cap@marvel.com', 'type': 'cycle', 'distance': 20, 'duration': 60},
            {'user': 'wonderwoman@dc.com', 'type': 'swim', 'distance': 2, 'duration': 40},
            {'user': 'batman@dc.com', 'type': 'run', 'distance': 10, 'duration': 50},
        ]
        db.activities.insert_many(activities)

        # Workouts
        workouts = [
            {'user': 'ironman@marvel.com', 'workout': 'Pushups', 'reps': 50},
            {'user': 'cap@marvel.com', 'workout': 'Situps', 'reps': 60},
            {'user': 'wonderwoman@dc.com', 'workout': 'Squats', 'reps': 70},
            {'user': 'batman@dc.com', 'workout': 'Pullups', 'reps': 30},
        ]
        db.workouts.insert_many(workouts)

        # Leaderboard
        leaderboard = [
            {'team': 'marvel', 'points': 200},
            {'team': 'dc', 'points': 180},
        ]
        db.leaderboard.insert_many(leaderboard)

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data.'))
