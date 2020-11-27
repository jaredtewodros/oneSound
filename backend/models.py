from django.db import models

# Create your models here.

# what is many to many, what is many to one

class Song(models.Model):
    album = models.TextField()
    artist = models.TextField()
    duration_ms = models.IntegerField()
    id = models.CharField()
    name = models.TextField()
    url = models.CharField()
    song_image = models.ImageField()
    # genres

class Album(models.Model):
    artist = models.TextField()
    # genre = models.CharField()
    id = models.CharField()
    album_image = models.ImageField()
    name = models.TextField()
    release_date = models.CharField()
    # tracks = models.ExpressionList()
    url = models.CharField()

class Artist(models.Model):
    # genres
    id = models.CharField()
    image = models.ImageField()
    name = models.CharField()
    url = models.CharField()