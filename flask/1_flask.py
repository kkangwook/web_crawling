##1. 기본구조
from flask import Flask

app=Flask(__name__)

@app.route('/')
def index():
    return 'hi'     #페이지 열면 hi만 출력

app.run()

#1-1. 하고 터미널에서 cd로 이 파일이 있는 디렉토리로 이동 후
# cd c:/doit/crawling-> python web_flask.py하고 엔터
# 주소뜨면 컨트롤+클릭으로 사이트 들어가면 hi뜸

#1-2. or 그냥 파이썬에서 실행하고 url클릭

##주의: 실행된 상태여야 페이지 정상작동->ctrl+c하고 url들어가면 안뜸
##또한 내부 수정하고 페이지 새로고침해도 안바뀜->껏다 다시켜야함
#  ㄴ이를 위해 옵션
app.run(debug=True)  #수정시 자동으로 껐다 켜줌->남들한테 배포할땐 모조건 꺼야 부하X



##2. 함수사용->동적으로: ex)랜덤 숫자 페이지에 출력해보기
import random

app=Flask(__name__)

@app.route('/')
def index():
    return str(random.random())     #출력값은 무조건 문자열만 가능
                                    #따라서 str로
app.run(debug=True)

#이러면 새로고침할때마다 매번 다른 랜덤값 나옴

#더 세련되게
@app.route('/')
def index():
    return 'random:<strong>'+str(random.random())+'</strong>'  #return은 무조건 ''안에 
                                # ㄴ함수쓰기 위해 ''밖에 쓰고 str화 하고 더하기
app.run(debug=True)
#이는 html상 'random:' <strong>0.221834927~</strong> 으로 나타나짐


##3. 라우팅: 어떤 주소를 누가 담당할것인가, 어떤 요청을 어떤 함수가 응답할것인가 연결시켜주는 작업
# route 데코레이터가 이 역할을 함
@app.route('/') # '/'만 돼있으면 어떤 사용자가 path를 입력하지않고 접속하면 이 밑의 함수가 작동
def index():
    return 'hi'


@app.route('/hello') # ~.com/hello로 접속하면 hello()함수가 작동
def hello():
    return 'hello, world'
app.run()        ## app.run()은 맨 밑에 딱 하나만!!!!


#라우팅시 변수삽입하는법
# ~.com/hello/1    #1번 id정보에 접속
#   하지만 2,3,4,~번에도 접속하고 싶다면?
# <>사용
@app.route('/hello/<id>')   #이 id는 변수로 다른이름도 상관X
def hello(id):
    return f'hello, world{id}'
app.run(debug=True)
# ~.com/hello/1로 접속하면 hello, world1,다른 숫자 n으로 접속하면 hello, worldn