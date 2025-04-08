from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from datetime import timedelta

class Command(BaseCommand):
    help = 'Populate the database with test data for users, teams, activities, leaderboard, and workouts'

    def handle(self, *args, **kwargs):
        # Create users
        users = [
            User(email='thundergod@mhigh.edu', name='Thor', password='password123'),
            User(email='metalgeek@mhigh.edu', name='Tony Stark', password='password123'),
            User(email='zerocool@mhigh.edu', name='Steve Rogers', password='password123'),
            User(email='crashoverride@mhigh.edu', name='Natasha Romanoff', password='password123'),
            User(email='sleeptoken@mhigh.edu', name='Bruce Banner', password='password123'),
        ]

        # Save users individually before clearing existing data
        for user in users:
            user.save()

        # Clear existing data after ensuring all users are saved
        # User.objects.all().delete()

        # Save users individually to ensure primary keys are assigned
        for user in users:
            user.save()

        # Create teams
        teams = [
            Team(name='Blue Team', members=[users[0].email, users[1].email]),
            Team(name='Gold Team', members=[users[2].email, users[3].email, users[4].email]),
        ]

        # Save teams individually to ensure they are saved before being referenced
        for team in teams:
            team.save()

        # Create leaderboard entries
        leaderboard_entries = [
            Leaderboard(team=teams[0], points=200),
            Leaderboard(team=teams[1], points=300),
        ]
        Leaderboard.objects.bulk_create(leaderboard_entries)

        # Create activities
        activities = [
            Activity(user=users[0], type='Cycling', duration=60, date='2025-04-08'),
            Activity(user=users[1], type='Crossfit', duration=120, date='2025-04-07'),
            Activity(user=users[2], type='Running', duration=90, date='2025-04-06'),
            Activity(user=users[3], type='Strength', duration=30, date='2025-04-05'),
            Activity(user=users[4], type='Swimming', duration=75, date='2025-04-04'),
        ]
        Activity.objects.bulk_create(activities)

        # Create workouts
        workouts = [
            Workout(name='Cycling Training', description='Training for a road cycling event'),
            Workout(name='Crossfit', description='Training for a crossfit competition'),
            Workout(name='Running Training', description='Training for a marathon'),
            Workout(name='Strength Training', description='Training for strength'),
            Workout(name='Swimming Training', description='Training for a swimming competition'),
        ]
        Workout.objects.bulk_create(workouts)

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data.'))