from django.shortcuts import render
from bs4 import BeautifulSoup
import requests


# Create your views here.

def index(request):
    idx = 0
    posts = []

    for i in range(2,5):
        if idx == 10 or idx == 21 or idx == 32:
            pass
        else:
            index_movie_url = 'https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=cnt&date=20200827'
            resp = requests.get(index_movie_url)
            soup_index_movie = BeautifulSoup(resp.content, 'html.parser')

            rangking_movie_select = soup_index_movie.select_one(f'#old_content > table > tbody > tr:nth-child({i}) > td.title > div > a').get('href')
            rangking_movie_title = soup_index_movie.select_one(f'#old_content > table > tbody > tr:nth-child({i}) > td.title > div > a').get_text()

            print(rangking_movie_title)
            rangking_movie_code = rangking_movie_select[rangking_movie_select.find('code=') + 5 : rangking_movie_select.find('code=') +11 ]

            print(rangking_movie_code)
            rangking_movie_detail_url = f'https://movie.naver.com/movie/bi/mi/basic.nhn?code={rangking_movie_code}'
            resp = requests.get(rangking_movie_detail_url)
            soup_movie_detail =  BeautifulSoup(resp.content, 'html.parser')

            detail_img_select = soup_movie_detail.select_one('#content > div.article > div.mv_info_area > div.poster > a > img').get('src')
            print(detail_img_select)

            posts.append({
                'movie_title':rangking_movie_title,
                'movie_img':detail_img_select,
                'movie_code':rangking_movie_code,
            })
        idx += 1


    context = {
        'posts': posts,
    }
    return render(request, 'index.html', context)

def result(request, movie):
    print(movie)
    print('result')
    return render(request, 'result.html')

