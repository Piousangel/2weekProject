# 2월5일까지 http://hyunseokmemo.shop  

## 사용 Stack
- Python, Jquery
- Bootstrap
- Flask
- MongoDB
- Robo 3T
- FileZilla
- Ubuntu
- .Shop domain

# 패키지사용

python3 -m venv .venv
source .venv/bin/activate
pip install requests  -> 패키지 설치
pip install beautifulsoup4 -> 웹스크래핑을 위해

brew tap mongodb/brew
brew install mongodb-community
brew services start mongodb-community
Project Interpreter에서 pymongo 패키지를 설치한다.
python 파일명.py

<h6 기본적으로 Flask 서버를 만들 때는 항상 프로젝트 폴더 안에 static, templates 폴더와 app.py를 만들고 시작합시다 >
### 메타데이터 스크래핑은 외울게요.

처음에 우분투 인스턴스 구매했어요..  
EC2 인스턴스에서 보안 ->Edit inbound rules 에 5000(TCP), 80(HTTP), 27017(TCP)포트 열어주고. 
http:// 내 ec2퍼블릭 ip:5000 해주세요. 

### 서버에 mongoDB 설치

wget -qO - https://www.mongodb.org/static/pgp/server-4.2.asc | sudo apt-key add -  
echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu bionic/mongodb-org/4.2 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-4.2.list
sudo apt-get update  
sudo apt-get install -y mongodb-org

### mongoDB 실행
sudo service mongod start

mongo     -> mongoDB 쉘 login 
input id/password  

use admin;  
db.createUser({user: "test", pwd: "test", roles["root"]});  

### Port forwarding
sudo iptables -t nat -A PREROUTING -i eth0 -p tcp --dport 80 -j REDIRECT --to-port 5000

### 원격 접속을 종료하더라도 서버가 계속 돌아가게 하기  
nohup python app.py &  

### 아래 명령어로 미리 pid 값(프로세스 번호)을 보고 프로세스 죽이기
ps -ef | grep 'app.py'  
kill -9 [pid값]
