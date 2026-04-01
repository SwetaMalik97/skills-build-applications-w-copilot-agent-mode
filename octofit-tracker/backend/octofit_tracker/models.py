from djongo import models

class Team(models.Model):
    _id = models.CharField(max_length=100, primary_key=True)
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, db_column='team')
    def __str__(self):
        return self.name

class Activity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, db_column='user')
    type = models.CharField(max_length=50)
    distance = models.FloatField()
    duration = models.IntegerField()
    def __str__(self):
        return f"{self.user} - {self.type}"

class Workout(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, db_column='user')
    workout = models.CharField(max_length=100)
    reps = models.IntegerField()
    def __str__(self):
        return f"{self.user} - {self.workout}"

class Leaderboard(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE, db_column='team')
    points = models.IntegerField()
    def __str__(self):
        return f"{self.team} - {self.points}"
