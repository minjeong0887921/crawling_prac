from django.contrib import admin

from parsed_data.models import Movies, Actors


@admin.register(Movies)
class MoviesAdmin(admin.ModelAdmin):
    pass


@admin.register(Actors)
class ActorsAdmin(admin.ModelAdmin):
    pass