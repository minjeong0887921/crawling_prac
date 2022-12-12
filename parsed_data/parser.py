from bs4 import BeautifulSoup
from selenium import webdriver
import time 

from parsed_data.models import Movies, Actors

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE","mysite.settings")
 
import django
django.setup()

# 웹드라이버 파일의 경로 
driver = webdriver.Chrome('chromedriver') 

def parse_blog():
    driver.get("https://movie.naver.com/movie/running/current.naver") 

    # 페이지 로딩 기다리기
    time.sleep(5)   

    # 페이지의 element 다 가져오기
    req = driver.page_source 

    # HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
    soup = BeautifulSoup(req, 'html.parser')

    movies = soup.select('#content > div.article > div > div.lst_wrap > ul > li')

    for movie in movies:
        image = movie.select('div > a > img')[0]['src']
        title = movie.select('div > a > img')[0]['alt']
        director = movie.select('dl > dd:nth-child(3) > dl > dd:nth-child(4) > span > a')[0].text
        _movie = Movies(title=title, director=director, image=image)
        _movie.save()

        casts = movie.select('dl > dd:nth-child(3) > dl > dd:nth-child(6) > span > a')
        for c in casts:
            name = Actors(name=c.text)
            name.save()
            _movie.Movies.add(name)
        
    # 끝나면 페이지 닫아주기
    driver.quit() 

if __name__=='__main__':
    parse_blog()