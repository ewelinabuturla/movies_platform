from django.contrib.postgres.fields import ArrayField
from django.contrib.postgres.fields import JSONField
from django.db import models

#Create your models here.
# Another comment

class Movies(models.Model):
    title = models.CharField('Title', max_length=60)
    year = models.CharField('Year', max_length=10, blank=True)
    rated = models.CharField('Rated', max_length=10, blank=True)
    released = models.CharField('Released', max_length=15, blank=True)
    runtime = models.CharField('Runtime', max_length=50, blank=True)
    genre = models.CharField('Genre', max_length=50, blank=True)
    director = models.CharField('Director', max_length=50, blank=True)
    writer = models.TextField('Writer', blank=True)
    actors = models.TextField('Actors', blank=True)
    plot = models.TextField('Plot', blank=True)
    language = models.CharField('Language', max_length=60, blank=True)
    country = models.CharField('Country', max_length=60, blank=True)
    awards = models.TextField('Awards', blank=True)
    poster = models.TextField('Poster', blank=True)
    metascore = models.CharField('Metascore', max_length=50, blank=True)
    imdbrating = models.CharField('imdbRating', max_length=50, blank=True)
    imdbvotes = models.CharField('imdbVotes', max_length=50, blank=True)
    imdbid = models.CharField('imdbID', max_length=40, blank=True)
    type = models.CharField('Type', max_length=40, blank=True)
    dvd = models.CharField('DVD', max_length=45, blank=True)
    boxoffice = models.CharField('BoxOffice', max_length=50, blank=True)
    production = models.CharField('Production', max_length=50, blank=True)
    website = models.CharField('Website', max_length=50, blank=True)
    response = models.CharField('Response', max_length=50, blank=True)
    ratings = JSONField(default=dict)

    def __str__(self):
        return f'{self.title} - {self.year}'

class Comments(models.Model):
    movie = models.ForeignKey(Movies, on_delete=models.CASCADE)
    comment = models.TextField('Comment')

    def __str__(self):
        return f'{self.movie} - {self.comment}'

    class Meta:
        ordering = ('movie',)
