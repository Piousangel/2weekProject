from pymongo import MongoClient           # pymongo를 임포트 하기 , 패키지 설치

client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아가기
db = client.dbsparta                      # 'dbsparta'라는 이름의 db 생성

# MongoDB에 insert 하기

# 'users'라는 collection에 {'name':'bobby','age':21}를 넣습니다.
db.users.insert_one({'name':'bobby','age':21})
db.users.insert_one({'name':'kay','age':27})
db.users.insert_one({'name':'john','age':30})