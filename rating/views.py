from django.shortcuts import render
from django.contrib import messages
from django.db.models import Q

from parsing.models import MovieData 


def get_queryset(self):
    search_keyword = self.request.GET.get('q', '')
    search_type = self.request.GET.get('type', '')
    movie_list = MovieData.objects.order_by('title')

    if search_keyword:
        if len(search_keyword) >= 1:
            if search_type == 'all':
                search_movie_list = movie_list.filter(Q (title__icontains=search_keyword) | Q (director__icontains=search_keyword) | Q (cast__icontains=search_keyword))
            elif search_type == 'title':
                search_movie_list = movie_list.filter(title__icontains=search_keyword)    
            elif search_type == 'director':
                search_movie_list = movie_list.filter(director__icontains=search_keyword)    
            elif search_type == 'cast':
                search_movie_list = movie_list.filter(cast__icontains=search_keyword)

            return search_movie_list
        else:
            messages.error(self.request, '검색어를 입력해주세요.')
    return movie_list
                