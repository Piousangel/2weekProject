from crypt import methods
from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient
client = MongoClient('localhos', 27017)
db = client.dbjungle

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/memo', methods=['GET'])
def listing():
    # 1. 모든 document 찾기 & _id 값은 출력에서 제외하기
    # 2. articles라는 키 값으로 영화정보 내려주기
    return jsonify({'result' : 'success', 'msg' : 'GET 연결되었습니다'})

## API 역할을 하는 영역
@app.route('/memo', methods['POST'])
def saving():
    # 1. 클라이언트로부터 데이터를 받기
	# 2. meta tag를 스크래핑하기
	# 3. mongoDB에 데이터 넣기
    return jsonify({'result' : 'success', 'msg' : 'POST 연결되었습니다'})

if __name__ == '__main__' :
    app.run('0,0,0,0' , port=5000, debug=True)
