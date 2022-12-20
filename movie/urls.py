from django.urls import path 

from movie import views 

app_name = 'movie'
urlpatterns = [
    path('current/', views.MovieLV.as_view(), name='movie_list'),
]