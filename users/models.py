from django.db import models
from django.contrib.auth.models import User

class User(models.Model):
    name = models.TextField()
# Create your models here.
