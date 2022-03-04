# 2월5일까지 http://hyunseokmemo.shop  

## 사용 Stack :stars:
- Python, Jquery
- Bootstrap
- Flask
- MongoDB
- Robo 3T
- FileZilla
- Ubuntu
- .Shop domain
---
- Node.js Express
- Bulma
- jinja2
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

~~~
render_params= {}
        render_params['이름아무거나'] = DB 아이디 or 받은 아이디
        return render_template('main.html', **render_params)
~~~

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

## Docker 사용법 (도커의 기본 명령어들):whale:

 :bulb:도커 버전 확인  
- docker -v

도커 이미지 다운만 받기
- docker pull {이미지명}:{태그}
- ex: docker pull python:3

컴퓨터 내 도커 이미지들 보기
- docker images

이미지로 컨테이너 생성하기
- docker create {옵션} {이미지명}:{태그}
- ex: docker create -it python

만들어진 컨테이너 시작하기 (이미지에 CMD로 지정해놓은 작업 시키기)
- docker start {컨테이너 id 또는 이름}

컨테이너로 들어가기 (컨테이너 내 CLI 이용하기)
- docker attach {컨테이너 id 또는 이름}

이미지를 다운 받아(없을 시에만) 바로 컨테이너 실행하여 진입하기
- docker run {이미지명}:{태그}
- ex: docker -it run python:3

|옵션|설명|
|:---|:---|
|-d|데몬으로 실행(뒤에서 - 안 보이는 곳(백그라운드)에서 알아서 돌라고 하기)|
|-it|컨테이너로 들어갔을 때 bash로 CLI 입출력을 사용할 수 있도록 해 줍니다|
|--name{이름}|컨테이너 이름 지정|
|-p {호스트의 포트 번호}:{컨테이너의 포트 번호}|호스트와 컨테이너의 포트를 연결합니다|
|--rm|컨테이너가 종료되면{내부에서 돌아가는 작업이 끝나면} 컨테이너를 제거합니다|
|-v {호스트의 디렉토리}:{컨테이너의 디렉토리}|호스트와 컨테이너의 디렉토리를 연결합니다

동작중인 컨테이너 재시작
- docker restart {컨테이너 id 또는 이름}

도커 컨테이너의 내부 쉘에서 빠져나오기 (컨테이너를 종료)
- exit or Ctrl + D

도커 컨테이너의 내부 쉘에서 빠져나오기 (컨테이너를 종료하지 않음)
- Ctrl + P,Q

동작중인 컨데이너들 보기
- docker ps (동작중이 아닌 것을 포함한 모든 컨테이너를 보려면 -a 옵션을 뒤에 붙입니다.

컨테이너 삭제
- docker rm {컨테이너 id 또는 이름}
- docer rm docker rm {컨테이너 id 또는 이름}
- docker rm `docker ps -a -q`

이미지 삭제 (컨테이너가 있을 시 강제삭제: -f 옵션 사용
- docker rmi {옵션} {이미지 id} 

#### 모든 컨테이너와 이미지 등 도커 요소 중지 및 사용  :bulb:
모든 컨테이너 중지
- docker stop $(docker ps -aq)
사용되지 않는 모든 도커 요소(컨테이너, 이미지, 네트워크, 볼륨 등) 삭제
- docker system prune -a
아래를 복붙하여 함께 실행하면 편리합니다.
- docker stop $(docker ps -aq)
- docker system prune -a

도커파일로 이미지 생성
- docker build -t {이미지명} .

도커 컴포즈 실행
- docker-compose 파일이 있는 디렉토리 기준
- docker-compose up
