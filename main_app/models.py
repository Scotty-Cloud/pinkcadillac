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

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('songs_detail', kwargs={'pk' : self.id})
  
# Create your models here.
class Movie(models.Model):
  name = models.CharField(max_length=100)
  description = models.CharField(max_length=250)
  recommend = models.CharField(max_length=25)
  # songs = models.ManyToManyField(Song)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse("movies_detail", kwargs={"pk": self.id})
  
class Release(models.Model):
  date = models.DateField("Release Date")
  enjoy = models.CharField(
    max_length=1,
    choices=ENJOY,
    default=ENJOY[0][0]
  )
  movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

  class Meta:
    ordering = ['-date']

  def __str__(self):
    return f"{self.get_enjoy_dispaly()} on {self.date}"

  

