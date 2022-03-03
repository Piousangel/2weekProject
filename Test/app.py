from crypt import methods
from flask import Flask, redirect, render_template, jsonify, request
import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient  

app = Flask(__name__)

client = MongoClient('localhost', 27017)   #mongodb://test:test@18.233.169.28  localhost
db = client.dbmemo


@app.route('/')
def home():
    return render_template('login.html', title = 'Login page')

@app.route('/create_form')
def create_form():
    return render_template('newform.html')
    
@app.route('/chk_id')
def check_id():

    id_receive = request.form['id_give']
    


    return b

# @app.route('/create_m')
# def create_m():
#     return a


@app.route('/memo', methods=['POST'])
def post_memo():
    
    title_receive = request.form['title_give']  
    comment_receive = request.form['comment_give']
    id_receive = request.form['id_give']
    password_receive = request.form['password_give'] 

    alonememo = {'title': title_receive, 'comment': comment_receive, 'user_id': id_receive, 'user_password': password_receive}

    db.memos.insert_one(alonememo)

    return jsonify({'result': 'success'})

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