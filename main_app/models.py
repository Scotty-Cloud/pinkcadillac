from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

ENJOY = (
  ("Y", "Of Course Yes are you MAD?"),
  ("N", "Nope because im a loser with no taste"),
  ("A", "ALWAYS, its ELVIS!!")
)

class Song(models.Model):
  name = models.CharField(max_length = 25)

# Create your models here.
