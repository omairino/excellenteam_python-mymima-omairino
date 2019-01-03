from django.db import models

class Artist(models.Model):
    artist_letter = models.CharField(max_length=50)


class Song(models.Model):
    song_letter = models.CharField(max_length=50)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)


class Fact(models.Model):
    fact_letter = models.TextField(max_length=2000)
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
