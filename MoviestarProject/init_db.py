import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient

client = MongoClient('localhos', 27017)
db = client.dbjungle

# DB에 저장할 영화인들의 출처 url 가져오기

def get_urls():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
    }
    data = requests.get('https://movie.naver.com/movie/sdb/rank/rpeople.nhn', headers=headers)
    soup = BeautifulSoup(data.text, 'html.parser')
    trs = soup.select('#old_content > table > tdoby > tr')

    url = []
    for tr in trs:
        a = tr.select_one('td.title > a')
        if a is not None:
            base_url = 'https://movie.naver.com/'
            url = base_url + a['href']
            urls.append(url)

    return urls

# 출처 url로 부터 영화인들의 사진, 이름, 최근작 정보를 가져오고 mystar 컬렉션에 저장
def insert_star(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
    }
    data = requests.get(url, headers=headers)
    soup = BeautifulSoup(data.text, 'html.parser')

    name = soup.select_one('#content > div.article > div.mv_info_area > div.mv_info.character > h3 > a').text
    img_url = soup.select_one('#content > div.article > div.mv_info_area > div.poster > img')['src']
    recent_work = soup.select_one(
        '#content > div.article > div.mv_info_area > div.mv_info.character > dl > dd > a:nth-child(1)').text

    doc = {
        'name' : name,
        'img_url' : img_url,
        'recent' : recent_work,
        'url' : url,
        'like' : 0
    }

    db.mystar.insert_one(doc)
    print('저장완료', name)

    def insert_all():
        db.mystar.drop()
        urls = get_urls()
        
        for url in urls:
            insert_star(url)

    ## 실행
    insert_all()