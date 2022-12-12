from django.contrib import admin

from movies.models import Movies, Actors


@admin.register(Movies)
class MoviesAdmin(admin.ModelAdmin):
    pass


@admin.register(Actors)
class ActorsAdmin(admin.ModelAdmin):
    pass