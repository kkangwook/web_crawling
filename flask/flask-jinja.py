## flask는 기본적으로 안에 jinja2 템플릿 엔진을 내장중이어서 import필요X !!!!
#render_template함수 사용
from flask import Flask, render_template

app=Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')   #index.html파일 가져옴
app.run()

## html파일 위치!!!!
/my_flask_app_folder   내가 만든 루트폴더
│-- app.py                이 폴더 안에 현재의 파이썬 파일
│-- /templates            루트 폴더에 templates라는 이름의 폴더 생성
│   │-- index.html            이 안에 html파일 필요!!!!!!!

## index.html파일 내부
<!DOCTYPE html>
<html>
<head>
    <title>사용자 페이지</title>
</head>
<body>
    <h1>안녕하세요, {{ username }}님!</h1>
</body>
</html>


## jinja2는 {{}}사용
## {{변수1}}  하고 변수1=안녕 하면 안녕이라는 값이 출력  
# 1. 값을 변수안에
@app.route('/')
def home():
    return render_template('index.html', username="홍길동")   #->안녕하세요 홍길동님! 으로 출
app.run()


## 2. 변수를 변수안에
@app.route('/user/<name>')   #여기있는 값이 들어감
def user(name):
    return render_template('user.html', username=name)   #url값을 body



## 3. 변수 여러개 넣기

--html 구조--
<body>    
    <p>이름: {{ user.name }}</p>
    <p>나이: {{ user.age }}</p>
    <p>도시: {{ user.city }}</p>
</body>

@app.route('/profile')
def profile():
    user_info = {'name': '홍길동', 'age': 25, 'city': '서울'}
    return render_template('profile.html', user=user_info)

# 이는 jinja2의 문법방식임
user.name → user_info['name'] (홍길동)
user.age → user_info['age'] (25)
user.city → user_info['city'] (서울)
즉, Jinja2에서 user.속성명은 user['속성명']과 같은 방식으로 동작


##4. 조건문 사용:   {%  %}형
템플릿내부:
<body>
    {% if name %}
        <h1>안녕하세요, {{ name }}님!</h1>
    {% else %}
        <h1>안녕하세요, 손님!</h1>
    {% endif %}
</body>

 의미: name값을 입력받았으면 위에꺼, 없으면 else, end if로 조건문 끝냄

## 파이썬과 동일하고 :만 없다고 보면됨
{% if number > 10 %}
    <p>값이 10보다 큽니다.</p>
{% elif 5 <= number <= 10 %}
    <p>값이 5 이상 10 이하입니다.</p>
{% else %}
    <p>값이 5보다 작습니다.</p>
{% endif %}


##5. 템플릿필터 '|' 사용
<p>{{ user_name | capitalize }}</p>    # user-name잎글자만 대문
<p>{{ user_name | lower }}</p>         
<p>{{ user_name | upper }}</p>  
<p>{{ user_name | truncate(5) }}</p>

***!!!!!!!!!!!!***
단순 값이 아닌 html구조로 넣고 싶다면
{{content | safe}}  로 해줘야지 문자열로 출력안되고 html구조로 출력
***!!!!!!!!!!!!***


##6. 반복문
<ul>
    {% for fruit in fruits %}
        <li>{{ fruit }}</li>
    {% endfor %}           #endfor사용
</ul>
그리고 render_template('profile.html', fruits=['apple','orange','melon']) 의 리스트 형태로

## 이때 while문은 지원하지 않음!!!!!

##7. macro(함수, def랑 같은 작용)
# html에서 매크로 만들고
{% macro input(name, value='', type='text') %}  #input이라는 이름과 파라미터들
    <input type="{{ type }}" name="{{ name }}" value="{{ value }}">  #얘네들이 들어감
{% endmacro %}  #끝낼때

#만든걸 다시 html에서 사용
<form>
    {{ input(name='unique_name', value='입력하시오',type='text') }}
</form>

결과: <input type="text" name="unique_name" value="입력하시오">가 form사이에 삽
