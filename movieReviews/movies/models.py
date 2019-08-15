from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
# Create your models here.


class Movies(models.Model):
    title = models.CharField(max_length=30)
    genres = models.CharField(max_length=50)
    class Meta:
        verbose_name = 'Movie'
        verbose_name_plural = 'Movies'

    def __str__(self):
        return self.title
    
    def __unicode__(self):
        return self.title


class Ratings(models.Model):
    userId = models.ForeignKey(User, on_delete=models.CASCADE)
    movieId = models.ForeignKey(Movies, on_delete=models.CASCADE)
    rating = models.FloatField()
    class Meta:
        verbose_name = 'Rating'
        verbose_name_plural = 'Ratings'
    
    def __str__(self):
        return str(self.movieId)
    
    def __unicode__(self):
        return self.movieId