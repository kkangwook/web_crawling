-남들이 들어올 수 있는 사이트 만들기
app.run(host='192.168.16.5', port=3179)
# http://192.168.16.5:3179/  남들이 치면 들어올 수 있음

----render template사용법----
html파일은 항상 templates폴더 안에->위치 지정시 templates는 쓸 필요 X
from flask import Flask, render_template

--기본
@app.route("/") 
def index() : # 응답 함수 
    return render_template('/step01/main.html') #templates안에 step01폴더안에 main.html을 가져오겠다

--이미지 가져오기
# {{ url_for('폴더위치',filename='~/~.jpg) }} 는 jinja2의 이미지 연결 표현
    #-> 웹문서의 경로가 바뀌어도 이미지 위치는 고정
<img src="{{ url_for('static', filename='images/ai.jpg') }}"/> 
# .py가 있는 위치에서 static=폴더위치 filename=그 폴더 안에서부터 디렉토리/파일명



--링크 이동
@app.route("/") 
def index() : # 응답 함수 
    return render_template('/step01/main.html')  

@app.route('/cont') 
def info() : # 응답 함수
    return render_template('/step01/cont.html') 
/cont로 이동 위해 main.html에 <a href='/cont'> cont로 이동</a> 서식이 존재
-> app.route(위치)에서 href=위치  하면 됌


-- jinja2 객체 가져오기
#html
<p> 사용자 이름 : {{name}} </p>

<p> 성적 </p>
{% for score in scores %}
    {% if score >= 70 %}
        <li> {{ score }} </li>
    {% endif %}
{% endfor %}

     #파이썬.py
@app.route("/view")
def view() :
    username = "홍길동"     #여기서 지정
    scores = [85, 65, 95]  
    return render_template('/step02/view.html',name=username, scores=scores) #여기에 넣음


-- jinja2로 app.route()파라미터에 전송 -> <>사용
#url.html
<a href='/url/{{ 객체 }}'>{{객체}}</a>
#python
@app.route('/url')
def tempo1()
    return render_template(file, 객체='홍길동')

->홍길동 링크 클릭->
@app.route('/url/<객체>')
def tempo2(객체):
    return render_template(newfile,변수=객체)


------form------
method지정 안해주면 defalut는 'get'

<form method='get' action='/'>일 경우
request.args.get('name')으로 가져올 수 있음

post는 request.form['name']

-->입력받은 변수 불러오기는 같은 라우트나 action에 의해 이동되는 라우트에서만 받을 수 있음
--> 그 외의 라우트에서 불러오는법: session(딕셔너리처럼 작동)
    from flask import session
    # a라우트
    a_value = request.form['name']
    session['name'] = a_value  # 세션에 값 저장
    #b라우트
    b_value=session.get('name', 'No name found') # 세션에서 값 가져오기
    
--form형식없이 url로 method는 get으로 정보전달
html파일
<a href="{{url_for('deptInfo',dno='30', dname='영업부', dloc='싱가폴')}}"> 30 </a>  #{{url_for(라우트주소, 변수='값}}'
이 30적힌링크 클릭하면(데이터 입력할 필요 없이 클릭)
.py
@app.route('/deptInfo', methods = ['GET']) # get 방식 전송 -defalut
def deptInfo() :   
    dno = request.args.get('dno') # 위의 변수들 받아옴
    dname = request.args.get('dname')
    dloc = request.args.get('dloc')
    # 템플릿에 값들 넘기기 
    return render_template('/exam03/dept_info.html', dno = dno, dname=dname, dloc=dloc)
