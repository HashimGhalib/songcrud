from django.db import models


class Artiste(models.Model):
    first_name = models.CharField(max_length=300, null=False)
    last_name = models.CharField(max_length=300, null=False)
    age = models.IntegerField(null=False)


class Song(models.Model):
    title = models.CharField(max_length=300, null=False)
    date_released = models.DateField(auto_now_add=True)
    likes = models.IntegerField
    artiste_id = models.ForeignKey(Artiste, on_delete=models.SET_DEFAULT)


class Lyric(models.Model):
    content = models.CharField(max_length=300, null=False)
    song_id = models.ForeignKey(Song, on_delete=models.SET_DEFAULT)
# Create your models here.
