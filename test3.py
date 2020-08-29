from bs4 import BeautifulSoup
import requests

headers = {
    'authority': 'movie.naver.com',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-dest': 'iframe',
    'referer': 'https://movie.naver.com/movie/bi/mi/point.nhn?code=189069',
    'accept-language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
    'cookie': 'NNB=D4IT6VFKZP5F4; NRTK=ag#20s_gr#2_ma#-2_si#0_en#0_sp#0; nx_ssl=2; NM_THUMB_PROMOTION_BLOCK=Y; page_uid=UyXTHsprvTossfz1yqossssstHG-297107; csrf_token=df34052d-fc21-4be1-bc3d-135fcf2ec947',
}

params = (
    ('code', '189069'),
    ('type', 'after'),
    ('isActualPointWriteExecute', 'false'),
    ('isMileageSubscriptionAlready', 'false'),
    ('isMileageSubscriptionReject', 'false'),
)

response = requests.get('https://movie.naver.com/movie/bi/mi/pointWriteFormList.nhn', headers=headers, params=params)

#NB. Original query string below. It seems impossible to parse and
#reproduce query strings 100% accurately so the one below is given
#in case the reproduced version is not "correct".
# response = requests.get('https://movie.naver.com/movie/bi/mi/pointWriteFormList.nhn?code=189069&type=after&isActualPointWriteExecute=false&isMileageSubscriptionAlready=false&isMileageSubscriptionReject=false', headers=headers)


soup = BeautifulSoup(response.text,'html.parser')

reviews = soup.select("div.score_result > ul > li")

for review in reviews:
    point = review.select_one("div.star_score > em").text
    comment = review.select_one("div.score_reple > p > span:nth-last-child(1)").text.strip()

    print(f'평점 : {point}')
    print(f'댓글 : {comment}')
    print()