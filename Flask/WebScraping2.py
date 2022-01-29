import requests
from bs4 import BeautifulSoup

# 타겟 URL을 읽어서 HTML를 받아옵니다..
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20200303',headers=headers)

# HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듭니다.
# soup이라는 변수에 "파싱 용이해진 html"이 담긴 상태가 됩니다.
# 이제 코딩을 통해 필요한 부분을 추출하면 됩니다.
soup = BeautifulSoup(data.text, 'html.parser')
# print(soup)  # HTML을 받아온 것을 확인할 수 있습니다.

movies = soup.select('#old_content > table > tbody > tr')
print(len(movies))

for movie in movies :
    print(movie)

# for movie in movies:
#     # movie 안에 a 가 있으면 조건을 만족하는 첫 번째 요소, 없으면 None을 반환
#     a_tag = movie.select_one('td.title > div > a')
#     print(a_tag)

# 개발자도구 Elements 탭에서 요소를 우클릭한 후 Copy > Copy selector를 해서 선택자를 얻을 수 있습니다

for movie in movies:
    # movie 안에 a가 있으면,
    a_tag = movie.select_one('td.title > div > a')
    score_tag = movie.select_one('td.point')
    
    if a_tag is not None:
        ranking = movie.select_one('td:nth-child(1) > img')['alt']
        print (ranking, a_tag.text , score_tag.text) 

# for movie in movies:
#     # movie 안에 a 가 있으면,
#     a_tag = movie.select_one('td.title > div > a')
#     if a_tag is not None:
#         # a의 text를 찍어본다.
#         rank = movie.select_one('td:nth-child(1) > img')['alt']  # img 태그의 alt 속성값을 가져오기
#         title = a_tag.text  # a 태그 사이의 텍스트를 가져오기
#         star = movie.select_one('td.point').text  # td 태그 사이의 텍스트를 가져오기
#         print(rank, title, star)

