from django.shortcuts import render
from django.contrib import messages
from django.db.models import Q
from django.views.generic import ListView

from parsing.models import Movie, Actor


class MovieLV(ListView):
    context_object_name = 'movie_list'
    queryset = Movie.objects.all()
    template_name = 'movie/movie_list.html'

    def get_queryset(self):
        search_keyword = self.request.GET.get('q', '')
        # search_type = self.request.GET.get('type', '')
        movie_list = Movie.objects.order_by('title')

        if search_keyword:
            if len(search_keyword) >= 1:
                search_movie_list = movie_list.filter(Q (title__icontains=search_keyword) | Q (director__icontains=search_keyword))
                return search_movie_list
            else:
                messages.error(self.request, '검색어를 입력해주세요.')
        return movie_list