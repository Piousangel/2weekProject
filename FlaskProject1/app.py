# 통상적으로 flask 서버를 돌리는 파일은 app.py라고 이름 짓습니다.

from flask import Flask
app = Flask(__name__)

@app.route('/')   #서버 실행시 기본페이지
def home():
    return 'This is Home!'

@app.route('/mypage')
def mypage():
    return 'This is My Page!'

if __name__ == '__main__' :
    app.run('0.0.0.0', port=5000, debug=True)