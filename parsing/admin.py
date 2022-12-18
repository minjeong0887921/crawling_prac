from django.contrib import admin
from django.utils.safestring import mark_safe

from parsing.models import Movie, Actor


@admin.register(Movie)
class MoviesAdmin(admin.ModelAdmin):
    list_display = ('_image', 'title', 'point', 'director', '_cast')

    def _cast(self, obj):
        return ', '.join([c.name for c in obj.cast.all()])
    _cast.short_description = 'cast'

    def _image(self, Movie):
        if Movie.image:
            return mark_safe(f'<img src="{Movie.image}" style="width: 72px;" />')
    _image.short_description = 'image'

    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related('cast')


@admin.register(Actor)
class ActorsAdmin(admin.ModelAdmin):
    list_display = ('_image', 'name')

    def _image(self, Actor):
        if Movie.image:
            return mark_safe(f'<img src="{Actor.image}" style="width: 72px;" />')
    _image.short_description = 'image'