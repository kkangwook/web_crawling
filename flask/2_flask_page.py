# 홈페이지 구현
#1. 기본 구조
from flask import Flask

app=Flask(__name__)

@app.route('/')    #가장 기본페이지
def index():       #모든 
    return '''<!doctype html>
    <html>
        <body>
            <h1><a href='/'>WEB</a><h1>
            <ol>
                <li><a href='/hello/1/'>여기를 각각 클릭하면</a></li>
                <li><a href='/hello/2/'>href주소로 가고</a></li>
                <li><a href='/hello/3/'>그 안에는 밑의 hello함수가 나오는 페이지로 이동</a></li>
            </ol>
            <h2>welcome</h2>
            hello, web
        </body>
    </html>
    '''

@app.route('/hello/<id>/') # 위에서 작동되기 위한 라우터 여기있음
def hello(id):     
    return f'hello, world{id}'
app.run(debug=True)

#2. 루프문들 활용

#데이터 셋 미리 만들어두기
## 실제로는 이렇게 안하고 데이터베이스에서 가져옴!!!!
data=[
    {'id':1,'title':'html','body':'html is ...'},
    {'id':2,'title':'css','body':'css is ...'},
    {'id':3,'title':'javascript','body':'javascript is ...'}
]


@app.route('/')    
def index():       
    data_lists=''
    for i in data:      # li, a태그와 href작성하고 주소 다시 ""로 감싸고 안에 {i["id"]}나 {i["title"]}로
        data_lists=data_lists+f'<li><a href="/hello/{i["id"]}/">{i["title"]}</a></li>'  #'이미 썼으므로 "로
    return f'''<!doctype html>
    <html>
        <body>
            <h1><a href='/'>WEB</a><h1>
            <ol>
                {data_lists}
            </ol>
            <h2>welcome</h2>
            hello, web
        </body>
    </html>
    '''

@app.route('/hello/<id>/') # 위에서 작동되기 위한 라우터 여기있음
def hello(id):     
    return f'hello, world{id}'
app.run(debug=True)