from djongo import models

class User(models.Model):
    user_id = models.ObjectIdField(primary_key=True)
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

class Team(models.Model):
    team_id = models.ObjectIdField(primary_key=True)
    name = models.CharField(max_length=255, unique=True)
    members = models.JSONField()

class Activity(models.Model):
    activity_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=255)
    duration = models.IntegerField()
    date = models.DateField()

class Leaderboard(models.Model):
    leaderboard_id = models.AutoField(primary_key=True)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    points = models.IntegerField()

class Workout(models.Model):
    workout_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
