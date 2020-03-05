from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Quize(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.title
class Enigma(models.Model):
    quize = models.ForeignKey(Quize, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    quize_type = models.IntegerField(default=0)
    def __str__(self):
            return self.text
class Option(models.Model):
    quize = models.ForeignKey(Enigma, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    correct = models.BooleanField(default=False)
    def __str__(self):
        return self.text + "  /  " + self.quize.text  