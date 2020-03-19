from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Quiz(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Riddle(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    quiz_type = models.IntegerField(default=0)

    def __str__(self):
        return self.text


class Option(models.Model):
    quiz = models.ForeignKey(Riddle, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    correct = models.BooleanField(default=False)

    def __str__(self):
        return self.text + "  /  " + self.quiz.text