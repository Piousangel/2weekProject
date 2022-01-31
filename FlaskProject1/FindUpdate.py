from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbjungle


score = db.movies.find_one({'title' : '매트릭스'})['star']
# print(score)

all_movies = list(db.movies.find({'star' : score}))

# # 영화 매트릭스와 평점이 같은 영화리스트 db에서 찾기
# for movie in all_movies:
#     print(movie['title'])

# 평점 0으로 수정
db.movies.update_one({'title' : '매트릭스'}, {'$set' : {'star' : '0'}})
user = db.movies.find_one({'title' : '매트릭스'})
print(user)

