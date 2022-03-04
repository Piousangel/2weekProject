from base64 import decode
from array import array
from crypt import methods
from datetime import datetime
from os import access
from flask import Flask, json, request, render_template, jsonify, redirect, url_for, session
import requests, random
import jwt
import datetime
from bs4 import BeautifulSoup
from pymongo import MongoClient  
from flask_bcrypt import Bcrypt
from functools import wraps

app = Flask(__name__)
# SECRET_KEY = 'abc'
app.config['SECRET_KEY'] = 'ABC123'
bcrypt = Bcrypt(app)
userInfo = MongoClient('localhost', 27017)   #mongodb://test:test@18.233.169.28  localhost
db = userInfo.dbclient

def check_for_token(func):
    @wraps(func)
    def wrapped(*args, **kwargs):
        token = request.args.get('my_access_token')
        if not token:
            print('there is no token')
            return redirect('/login2')
        try:
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
        except:
            print('token invalid')
            return redirect('/login2')
        return func(*args, **kwargs)
    return wrapped

# @app.route('/chk_token')
# def token():
#     token_receive = request.cookies.get('mytoken')
#     try:
#         payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
#         user_info = db.userInfo.find_one({"user_id" : payload['user_id']})
#     except jwt.ExpiredSignatureError:
#         return redirect(url_for("login", msg="로그인 시간이 만료되었습니다."))
#     except jwt.exceptions.DecodeError:
#         return redirect(url_for("login", msg="로그인 정보가 존재하지 않습니다."))

@app.route('/')
def home():
    return render_template('login2.html', title = 'Login page')

@app.route('/home')
def welcome():
    return render_template('login2.html')

@app.route('/create_form', methods=['GET'])
def create_form():
    return render_template('newform.html', title = 'NewForm page')
    # return jsonify({'result': 'success', 'html_name': 'newform.html'})

# @app.route('/logincheck', methods=['GET'])
# @check_for_token
# def logincheck():
#     if session['logged_in'] == True :
#         user_token = request.args.get('my_access_token')
#         decoded = jwt.decode(user_token, app.config['SECRET_KEY'], algorithms=["HS256"])
#         doc = {'user_id':decoded['id']}
#         return redirect('/main')
#     else :
#         return redirect('/home')

@app.route('/confirm_user', methods = ['POST'])
def login_user() :
    id_receive = request.form['id_give']
    pw_receive = request.form['password_give']
    # print(id_receive, pw_receive)
    user_info = db.userInfo.find_one({'user_id' : id_receive})
    # print(user_info)
    try:
        if bcrypt.check_password_hash(user_info['user_password'], pw_receive) :
        # print(bcrypt.check_password_hash(user_info['user_password'], pw_receive))
        # render_params = {}
        # render_params['id'] = id_receive
        # **render_params,
            access_payload = {"id": id_receive, "exp": datetime.datetime.utcnow() + datetime.timedelta(seconds=30)}
            # session['logged_in'] = True
            # return jsonify({"result": "success", 'access_token': jwt.encode(access_payload, app.config['SECRET_KEY'], algorithm="HS256")})
            return jsonify({"result": "success"})
        else:
            return jsonify({"result": "fail"})
    except:
        print("Tlqkf???")
        return jsonify({"result": "exception!"})

@app.route('/create_m', methods = ['POST'])
def create_m():
    name_receive = request.form['name_give']
    id_receive = request.form['id_give']
    password_receive = request.form['password_give']
    pw_hash = bcrypt.generate_password_hash(password_receive)
    try:
        createform = {'user_name': name_receive, 'user_id': id_receive, 'user_password' : pw_hash}
        db.userInfo.insert_one(createform)
        return jsonify({'result': 'success'})
    except:
        return jsonify({'result': 'fail'})

@app.route('/main')
def mainhome() :
    return render_template('main2.html')
    
@app.route('/chk_idOverlapping', methods=['POST'])
def check_idOverlapping():
    id_receive = request.form['id_give']
    # db_ID = db.getCollection('userInfo').find({"user_name":"id_receive"})
    db_id = db.userInfo.find_one({'user_id' : id_receive})
    if db_id is None :
        return jsonify({'result': 'success'})
    else :
        return jsonify({'result': 'fail'})
    
# @app.route('/create_m', methods=['GET', 'POST'])
# def create_m():
#     if request.method == 'POST':
#         name_receive = request.form['name_give']
#         id_receive = request.form['id_give']
#         password_receive = request.form['password_give']

#         createform = {'user_name': name_receive, 'user_id': id_receive, 'user_password' : password_receive}
#         db.userInfo.insert_one(createform)
#         return render_template('login.html')
#     else :

#         return render_template('login.html')
#         # return jsonify({'result': 'success'})




# @app.route('/memo', methods=['POST'])
# def post_memo():
    
#     title_receive = request.form['title_give']  
#     comment_receive = request.form['comment_give']
#     id_receive = request.form['id_give']
#     password_receive = request.form['password_give'] 

#     alonememo = {'title': title_receive, 'comment': comment_receive, 'user_id': id_receive, 'user_password': password_receive}

#     db.memos.insert_one(alonememo)

    
@app.route('/edit', methods=['POST'])
def edit_memo():

    existing = request.form['existing_give']
    title_receive = request.form['title_give']  
    comment_receive = request.form['comment_give']
    password_receive = request.form['password_give']

    new_title = title_receive
    new_comment = comment_receive
    
    db.memos.update_one({'title': existing}, {'$set': {'title': new_title}})
    db.memos.update_one({'title': new_title}, {'$set': {'comment': new_comment}})
    
    return jsonify({'result': 'success'})


@app.route('/delete', methods=['POST'])
def delete_memo():
    title_receive = request.form['title_give']

    db.memos.delete_one({'title': title_receive})

    return jsonify({'result': 'success'})


@app.route('/memo', methods=['GET'])      # window.location.reload(); 시 GET
def read_articles():
    result = list(db.memos.find({}, {'_id': 0}))
    return jsonify({'result': 'success', 'articles': result})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)