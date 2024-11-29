from django.db import models
from django.contrib.auth.models import User

class Player(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=63)
    high_score = models.IntegerField(default=0)


class Type(models.Model):
    name = models.CharField(max_length=63)

class Task(models.Model):
    description = models.TextField()
    max_score = models.IntegerField()
    difficulty = models.IntegerField()
    type = models.ForeignKey(Type, on_delete=models.CASCADE)


class PlayerTask(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)
    score = models.IntegerField(default=0)
    last_updated = models.DateTimeField(auto_now=True)

class TaskAnswer(models.Model):
    answer = models.CharField(max_length=63)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
