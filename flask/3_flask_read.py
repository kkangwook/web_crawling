##1. read

from flask import Flask

app=Flask(__name__)


data=[
    {'id':1,'title':'html','body':'html is ...'},
    {'id':2,'title':'css','body':'css is ...'},
    {'id':3,'title':'javascript','body':'javascript is ...'}
]


@app.route('/')    
def index():       
    data_lists=''
    for i in data:      
        data_lists=data_lists+f'<li><a href="/read/{i["id"]}/">{i["title"]}</a></li>' 
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
                    ##
@app.route('/read/<int:id>/')   #그냥 id는 str값-> 밑에 ==문 사용위해 int로
def read(id):     
    data_lists=''
    for i in data:      
        data_lists=data_lists+f'<li><a href="/read/{i["id"]}/">{i["title"]}</a></li>' 
    title=''
    body=''

    for i in data:
        if id==i['id']:
            title=i['title']
            body=i['body']
    return f'''<!doctype html>
    <html>
        <body>
            <h1><a href='/'>WEB</a><h1>
            <ol>
                {data_lists}
            </ol>
            <h2>{title}</h2>
            {body}
        </body>
    </html>
    '''
## html클릭하면 html정보가, css는 css, javascript는 javascript


##2. 간단화:return 부분을 함수안에 

#들어있는 링크 부분들 함수화
def getcontent():
    data_lists=''
    for i in data:      
        data_lists=data_lists+f'<li><a href="/read/{i["id"]}/">{i["title"]}</a></li>'     
    return data_lists

# html구조 함수화
def template(list,content):
    return f'''<!doctype html>
    <html>
        <body>
            <h1><a href='/'>WEB</a><h1>
            <ol>
                {list}
            </ol>
            {content}
        </body>
    </html>
    '''    


#위의 두 함수 사용해서 간략화
@app.route('/')    
def index():       
    return template(getcontent(),'<h2>welcome</h2>hellow,WEB')


@app.route('/read/<int:id>/')   #그냥 id는 str값-> 밑에 ==문 사용위해 int로
def read(id):     
    data_lists=''
    for i in data:      
        data_lists=data_lists+f'<li><a href="/read/{i["id"]}/">{i["title"]}</a></li>' 
    title=''
    body=''

    for i in data:
        if id==i['id']:
            title=i['title']
            body=i['body']
    return template(data_lists,f'<h2>{body}')
app.run(debug=True)