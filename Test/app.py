from crypt import methods
from flask import Flask, redirect, render_template, jsonify, request
import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient  

app = Flask(__name__)

userInfo = MongoClient('localhost', 27017)   #mongodb://test:test@18.233.169.28  localhost
db = userInfo.dbclient

@app.route('/')
def home():
    return render_template('login2.html', title = 'Login page')

@app.route('/create_form', methods=['GET'])
def create_form():
    return render_template('newform.html', title = 'NewForm page')
    # return jsonify({'result': 'success', 'html_name': 'newform.html'})

@app.route('/confirm_user', methods=['GET','POST'])
def login_user():
    if request.method == 'POST':
        id_receive = request.form['id_give']
        pw_receive = request.form['id_give']

        id = db.getCollection('userInfo').find({"user_id":"id_receive"})
        if id == id_receive :
            pw = db.getCollection('userInfo').find({"user_password":"pw_receive"})
            if pw == pw_receive :
                return jsonify({'result': 'success'})
        else :
                return jsonify({'result': 'fail'})
    else :
        return render_template('main2.html')
    
@app.route('/chk_id')
def check_id():

    id_receive = request.form['id_give']
    
    name = db.getCollection('userInfo').find({"user_name":"id_receive"})
    if name is None :
        return jsonify({'result': 'success'})
    else :
        return jsonify({'result': 'fail'})
    

@app.route('/create_m', methods=['GET', 'POST'])
def create_m():
    if request.method == 'POST':
        name_receive = request.form['name_give']
        id_receive = request.form['id_give']
        password_receive = request.form['password_give']

        createform = {'user_name': name_receive, 'user_id': id_receive, 'user_password' : password_receive}
        db.userInfo.insert_one(createform)
        return render_template('login.html')
    else :

        return render_template('login.html')
        # return jsonify({'result': 'success'})



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