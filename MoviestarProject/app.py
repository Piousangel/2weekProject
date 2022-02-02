from pymongo import MongoClient

from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

client = MongoClient('localhost', 27017)      #나중에 'mongodb://test:test@아이피'
db = client.dbjungle


# HTML 화면 보여주기 
@app.route('/')
def home():
    return render_template('index.html')


# API 역할을 하는 부분
@app.route('/api/list', methods=['GET'])
def show_stars():
    # 1. db에서 mystar 목록 전체를 검색 ID는 제외하고 like 가 많은 순으로 정렬
    # 참고) find({},{'_id':False}), sort() 사용
    stars = list(db.mystar.find({}, {'_id': False}).sort('like', -1))
    # 2. 성공하면 success 메시지와 함께 stars_list 목록을 클라이언트에 전달
    return jsonify({'result': 'success', 'stars_list': stars})


@app.route('/api/like', methods=['POST'])
def like_star():
    # 1. 클라이언트가 전달한 name_give를 변수에 저장
    name_receive = request.form['name_give']
    # 2. mystar 목록에서 find_one 사용
    star = db.mystar.find_one({'name': name_receive})

    new_like = star['like'] + 1

    # 3. mystar 목록에서 name이 name_receive인 문서의 like 업뎃  '$set'사용
    
    db.mystar.update_one({'name': name_receive}, {'$set': {'like': new_like}})
    # success 메시지를 반환합니다.
    return jsonify({'result': 'success'})


@app.route('/api/delete', methods=['POST'])
def delete_star():

    name_receive = request.form['name_give']
    # name이 name_receive와 일치하는 star를 제거합니다.
    db.mystar.delete_one({'name': name_receive})
    #success 메시지 리턴
    return jsonify({'result': 'success'})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)