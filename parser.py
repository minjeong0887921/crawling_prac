from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import time 

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE","mysite.settings")

import django
django.setup()

from parsing.models import MovieData, ActorData

# 웹드라이버 파일의 경로 

def movie_parsing():
    driver = webdriver.Chrome('/path/to/chromedriver') 

    driver.get("https://movie.naver.com/movie/running/current.naver") 

    # 페이지 로딩 기다리기
    time.sleep(5)   

    req = driver.page_source 
    soup = BeautifulSoup(req, 'html.parser')

    movies = soup.select('#content > div.article > div > div.lst_wrap > ul > li')

    for movie in movies:
        image = movie.select('div > a > img')[0]['src']
        title = movie.select('div > a > img')[0]['alt']
        director = movie.select('dl > dd:nth-child(3) > dl > dd:nth-child(4) > span > a')[0].text
        _movie = MovieData(title=title, director=director, image=image)
        _movie.save()

        casts = movie.select('dl > dd:nth-child(3) > dl > dd:nth-child(6) > span > a')
        for c in casts:
            req = requests.get('https://movie.naver.com/' + c['href'])
            html = req.text 
            soup = BeautifulSoup(html, 'html.parser')
            image = soup.select('#content > div.article > div.mv_info_area > div.poster > img')[0]['src']
            
            actor = ActorData(name=c.text, image=image)
            actor.save()
            _movie.cast.add(actor)
    
    driver.quit() 
    return 


if __name__=='__main__':
    movie_parsing()