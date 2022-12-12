from django.db import models


class Movies(models.Model):
    title = models.CharField('TITLE', max_length=200)
    director = models.CharField('DIRECTOR', max_length=50)
    cast = models.ManyToManyField('Actors', blank=True)
    image = models.ImageField('IMAGE')

    def __str__(self):
        return self.title 


class Actors(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name