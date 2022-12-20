from django.db import models


class Movie(models.Model):
    title = models.CharField('TITLE', max_length=200)
    director = models.CharField('DIRECTOR', max_length=50)
    cast = models.ManyToManyField('ACTOR', blank=True)
    image = models.ImageField('IMAGE')
    rating = models.FloatField('rating')

    def __str__(self):
        return self.title 


class Actor(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField()

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name