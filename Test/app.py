from base64 import decode
from array import array
from crypt import methods
from datetime import datetime
from email import message
from os import access
from flask import Flask, json, request, render_template, jsonify, redirect, url_for, session
import jwt
import datetime
from bs4 import BeautifulSoup
from pymongo import MongoClient  
from bson import ObjectId
import bcrypt

app = Flask(__name__)
# SECRET_KEY = 'abc'
# app.config['SECRET_KEY'] = 'ABC123'
app.secret_key = 'ABC123'
# bcrypt = Bcrypt(app)
userInfo = MongoClient('localhost', 27017)   #mongodb://test:test@18.233.169.28  localhost
db = userInfo.dbclient

@app.route('/')
def home():
    if session.get("logged_in"):
        print("logout!!!!!!")
        return render_template("main.html")
    else :  
        return render_template('login2.html', title = 'Login page')

@app.route('/home')
def welcome():
    return render_template('main.html')

@app.route('/create_form', methods=['GET'])
def create_form():
    return render_template('newform.html', title = 'NewForm page')
    # return jsonify({'result': 'success', 'html_name': 'newform.html'})


@app.route('/confirm_user', methods=['GET', 'POST'])
def login_user():
    if request.method == 'POST' :
        id_receive = request.form['id_give']
        pw_receive = request.form['password_give']
        user_info = db.userInfo.find_one({'user_id' : id_receive})

        if user_info is not None :
            id_val = user_info['user_id']
            name_val = user_info['user_name']
            passwordchk = user_info['user_password']
            if bcrypt.checkpw(pw_receive.encode('utf-8'), passwordchk) :
                session['logged_in'] = True 
                session['user_id'] = id_val
                session['user_name'] = name_val
                return jsonify({'result' : 'success'})
            else :
                return jsonify({'result' : 'fail'})
        else :
            return jsonify({'result' : 'fail'})


# @app.route('/confirm_user', methods = ['POST'])
# def login_user() :
#     id_receive = request.form['id_give']
#     pw_receive = request.form['password_give']
#     # print(id_receive, pw_receive)
#     user_info = db.userInfo.find_one({'user_id' : id_receive})
#     # print(user_info)
#     try:
#         if bcrypt.check_password_hash(user_info['user_password'], pw_receive) :
#         # print(bcrypt.check_password_hash(user_info['user_password'], pw_receive))
#         # render_params = {}
#         # render_params['id'] = id_receive
#         # **render_params,
#             access_payload = {"id": id_receive, "exp": datetime.datetime.utcnow() + datetime.timedelta(seconds=30)}
#             # session['logged_in'] = True
#             # return jsonify({"result": "success", 'access_token': jwt.encode(access_payload, app.config['SECRET_KEY'], algorithm="HS256")})
#             return jsonify({"result": "success"})
#         else:
#             return jsonify({"result": "fail"})
#     except:
#         print("Tlqkf???")
#         return jsonify({"result": "exception!"})

@app.route('/create_m', methods = ['POST'])
def create_m():
    name_receive = request.form['name_give']
    id_receive = request.form['id_give']
    password_receive = request.form['password_give']
    pw_hash = bcrypt.hashpw(password_receive.encode('utf-8'), bcrypt.gensalt())
    # bcrypt.generate_password_hash(password_receive)
    try:
        createform = {'user_name': name_receive, 'user_id': id_receive, 'user_password' : pw_hash}
        db.userInfo.insert_one(createform)
        return jsonify({'result': 'success'})
    except:
        return jsonify({'result': 'fail'})

@app.route('/chk_idOverlapping', methods=['POST'])
def check_idOverlapping():
    id_receive = request.form['id_give']
    # db_ID = db.getCollection('userInfo').find({"user_name":"id_receive"})
    db_id = db.userInfo.find_one({'user_id' : id_receive})
    if db_id is None :
        return jsonify({'result': 'success'})
    else :
        return jsonify({'result': 'fail'})
    
@app.route('/logout', methods=['GET'])
def logout():
    session['logged_in'] = False
    return redirect(url_for('home'))

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