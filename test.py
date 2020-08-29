from bs4 import BeautifulSoup
import requests

# 페이지 접근 range에서 범위 설정해주면 됨
for page_num in range(1,2):
    review_url = f'https://movie.naver.com/movie/point/af/list.nhn?&page={page_num}'
    resp = requests.get(review_url)
    soup_01 = BeautifulSoup(resp.content, 'html.parser')

    # 페이지 안에서 평점하나하나씩 접근
    for child_num in range(1,11):
        print(page_num, child_num)
        movie_line = soup_01.select_one(f'#old_content > table > colgroup > tbody > tr:nth-child({child_num}) > td.title').get_text()

        movie_title = movie_line[0 : movie_line.find('별점')].strip()
        movie_score = movie_line[movie_line.find('점 중') + 3 : movie_line.find('점 중') + 6].strip()
        movie_review = movie_line[movie_line.find('점 중') + 5 : movie_line.find('점 중') + len(movie_line)-45].strip()

        print(f'영화제목:{movie_title}')
        print(f'평점:{movie_score}')
        print(f'영화리뷰:{movie_review}')
        # 영화 장르 크롤링
        movie_genre = soup_01.select_one(f'#old_content > table > colgroup > tbody > tr:nth-child({child_num}) > td.title > a.movie.color_b').get('href')
        movie_genre2 = movie_genre[movie_genre.find('sword=')+6 : movie_genre.find('sword=')+12]
        print(f'영화장르넘버:{movie_genre2}')

        genre_url = f'https://movie.naver.com/movie/point/af/list.nhn?st=mcode&sword={movie_genre2}&target=after'
        print(genre_url)
        resp = requests.get(genre_url)
        soup_genre = BeautifulSoup(resp.content, 'html.parser')

        genre = ''
        for i in range(2):
            movie_genre3 = soup_genre.select_one(f'#old_content > div.choice_movie_box > div.choice_movie_info > table > tr > td > a:nth-child({i+1})').get('href')

            if movie_genre3[movie_genre3.find('nhn?')+4 : movie_genre3.find('nhn?') +9] == 'genre':
                soup_genre4 = soup_genre.select_one(f'#old_content > div.choice_movie_box > div.choice_movie_info > table > tr > td > a:nth-child({i+1})').get_text()
                genre += f'{soup_genre4} '
            else:
                break
        print(f'영화장르:{genre}')
        
        # 해당리뷰 작성자를 따라가서 작성한 모든리뷰 확인
        user_num = soup_01.select_one(f'#old_content > table > colgroup > tbody > tr:nth-child({child_num}) > td:nth-child(3) > a').get('href')[33:41]
        b_url = f'https://movie.naver.com/movie/point/af/list.nhn?st=nickname&sword={user_num}&target=after'
        resp = requests.get(b_url)
        soup_02 = BeautifulSoup(resp.content, 'html.parser')
        
        print(f'{user_num}이 작성한 리뷰들@@@@')
        for i in range(1,11):
            try:
                b = soup_02.select_one(f'#old_content > table > colgroup > tbody > tr:nth-child({i}) > td.title').get_text()
                movie_review = b[b.find('점 중') + 5:b.find('점 중') + len(b)-45].strip()
                print(f'영화리뷰:{movie_review}')
            except:
                break
        

