from django.contrib import admin
from django.utils.safestring import mark_safe

from parsing.models import MovieData, ActorData


@admin.register(MovieData)
class MoviesAdmin(admin.ModelAdmin):
    list_display = ('_image', 'title', 'director', '_cast')

    def _cast(self, obj):
        return ', '.join([c.name for c in obj.cast.all()])
    _cast.short_description = 'cast'

    def _image(self, MovieData):
        if MovieData.image:
            return mark_safe(f'<img src="{MovieData.image}" style="width: 72px;" />')
    _image.short_description = 'image'

    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related('cast')


@admin.register(ActorData)
class ActorsAdmin(admin.ModelAdmin):
    list_display = ('_image', 'name')

    def _image(self, ActorData):
        if MovieData.image:
            return mark_safe(f'<img src="{ActorData.image}" style="width: 72px;" />')
    _image.short_description = 'image'