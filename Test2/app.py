from flask import Flask, render_template, jsonify, request, session, redirect, url_for
from pymongo import MongoClient  
from bson import ObjectId
import jwt
import requests

app = Flask(__name__)
client = MongoClient('localhost', 27017)
db = client.session  

@app.route('/')
def home():
    # """Session control"""
        # return render_template('login.html')

    if session.get('logged_in'):
        return render_template('home.html')
    else:
        return render_template('login.html')
    

@app.route('/login', methods=['POST'])
def login():
    username = request.form['id_give']
    password = request.form['password_give'] 
    user = db.session.find_one({'username':username})
    if user:
        db_password = jwt.decode(user['password'], 'abc', algorithm="HS256")['password']
        if password == db_password:
            session['logged_in'] = True
            session['name'] = user['username']
            session['sort_order'] = 'time'
            return jsonify({'result': 'success'})
    return jsonify({'result': 'fail'})

@app.route('/register/')
def register():
    return render_template('register.html')

@app.route('/register/add', methods=['POST'])
def add_user():
    before_password = request.form['password_give']
    after_password = jwt.encode({'password': before_password}, 'abc', algorithm='HS256')
    print(after_password)
    new_user = {'username':request.form['id_give'], 'password':after_password}
    print(new_user)
    if list(db.session.find({'username':request.form['id_give']})):
        return jsonify({'result': 'overlap'})
    else:
        db.session.insert_one(new_user)
        return jsonify({'result': 'success'})

@app.route('/home')
def main():
    return render_template('home.html')

@app.route('/home/post', methods=['POST'])
def post_memo():
    id_receive = request.form['id_give']  
    memo_receive = request.form['memo_give']
    date_recieve = request.form['date_give']  
    anonymous_receive = request.form['anonymous']
    memo = {'id': id_receive, 'memo': memo_receive, 'date': date_recieve, 'anonymous': anonymous_receive, 'like': 0, 'dislike': 0, 'like_id' : "", 'dislike_id':""}

    db.memos.insert_one(memo)
    return jsonify({'result': 'success'})

@app.route('/home/read', methods=['GET'])
def read_memos():
    if session['sort_order'] == 'time':
        result = list(db.memos.find({}))
    elif session['sort_order'] == 'time_old':
        result = list(db.memos.find({}))
        result.reverse()
    elif session['sort_order'] == 'mine':
        result = list(db.memos.find({'id':session['name']}))
    elif session['sort_order'] == 'like':
        result = list(db.memos.find({}).sort("like",1))
    elif session['sort_order'] == 'dislike':
        result = list(db.memos.find({}).sort("dislike",1))

    for data in result:
        data['_id'] = str(data['_id'])
    return jsonify({'result': 'success', 'memos': result})

@app.route('/home/delete', methods=['POST'])
def delete_memos():
    db_id_receive = request.form['db_id_give']
    object_id = ObjectId(db_id_receive)
    db.memos.delete_one({'_id' : object_id})
    return jsonify({'result': 'success'})

@app.route('/home/update', methods=['POST'])
def update_memos():
    db_id_receive = request.form['db_id_give']
    new_memo_receive = request.form['new_memo']
    new_time_receive = request.form['new_time'] + '(수정)'
    object_id = ObjectId(db_id_receive)
    db.memos.update_one({'_id' : object_id},{'$set':{'memo':new_memo_receive}})
    db.memos.update_one({'_id' : object_id},{'$set':{'date':new_time_receive}})
    return jsonify({'result': 'success'})

@app.route('/home/like', methods=['POST'])
def like_memos():
    db_id_receive = request.form['db_id_give']
    user_id_receive = request.form['id_give']
    object_id = ObjectId(db_id_receive)
    memo = db.memos.find_one({'_id' : object_id})
    print(user_id_receive)
    print(memo['like_id'].split(','))
    if user_id_receive in memo['like_id'].split(','):
        return jsonify({'result': 'fail'})
    else: new_like = memo['like'] + 1
    db.memos.update_one({'_id' : object_id}, {'$set':{'like':new_like}})
    like_id = memo['like_id']
    new_like_id = like_id + ',' + user_id_receive
    db.memos.update_one({'_id' : object_id}, {'$set':{'like_id':new_like_id}})
    return jsonify({'result': 'success'})


@app.route('/home/sort', methods=['POST'])
def sort_memos():
    sort_order_receive = request.form['sort_order_give']
    session['sort_order'] = sort_order_receive

    return jsonify({'result': 'success'})
    
@app.route('/home/dislike', methods=['POST'])
def dislike_memos():
    db_id_receive = request.form['db_id_give']
    user_id_receive = request.form['id_give']
    object_id = ObjectId(db_id_receive)
    memo = db.memos.find_one({'_id' : object_id})
    if user_id_receive in memo['dislike_id'].split(','):
        return jsonify({'result': 'fail'})
    else: new_dislike = memo['dislike'] + 1
    db.memos.update_one({'_id' : object_id}, {'$set':{'dislike':new_dislike}})
    dislike_id = memo['dislike_id']
    new_dislike_id = dislike_id + ',' + user_id_receive
    db.memos.update_one({'_id' : object_id}, {'$set':{'dislike_id':new_dislike_id}})
    return jsonify({'result': 'success'})

@app.route("/logout")
def logout():
	"""Logout Form"""
	session['logged_in'] = False
	return redirect(url_for('home'))

if __name__ == '__main__':  
    app.secret_key = "123"
    app.run('0.0.0.0', port=5000, debug=True)