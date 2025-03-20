## create
#정보 입력 받아 서버로 전송
# request함수 필요-입력받은 정보 관리
# redirect: 해당 url로 강제로 이동시켜줌
from flask import Flask, request, redirect

app=Flask(__name__)

data=[
    {'id':1,'title':'html','body':'html is ...'},
    {'id':2,'title':'css','body':'css is ...'},
    {'id':3,'title':'javascript','body':'javascript is ...'}
]



def getcontent():
    data_lists=''
    for i in data:      
        data_lists=data_lists+f'<li><a href="/read/{i["id"]}/">{i["title"]}</a></li>'     
    return data_lists


def template(list,content):
    return f'''<!doctype html>
    <html>
        <body>
            <h1><a href='/'>WEB</a><h1>
            <ol>
                {list}
            </ol>
            {content}
            <ul>
                <li><a href='/create/'>create</a></li>      #여기에  create칸 생성
            </ul>
        </body>
    </html>
    '''    

## <input>은 입력할 수 있는 창을 만들어줌
#input의 속성:
    #1. type=text, click, button등
    #2. placeholder='빈칸에 표시될 말들'
    #3. type='submit': 제출버튼 생성, 안의 value값으로 버튼 이름 정함
## <textarea>:글자 넣을 수 있는 큰 네모빈칸 생성

## name속성과 value속성으로 key:value형태로 저장

##그리고 이 받은 값들을 지정한곳에 전해주는데 필요한 태그가 <form>
# <form>태그의 action속성: 이동할url지정
# method=GET(default이며 url에 name과 value포함됨) or POST(은밀한 payload방식으로 서버로 안전하게 전송)

#flask의 request함수
    # request.method: get인지 post인지
    #request.form['name]: 해당 name의 input태그에서 입력받은 값 반환
nextid=4  #앞으로 새로운 값 입력받을때마다 4에서부터 1씩 증가할 id값



#입력받을 수 있는 페이지 만들기!!!
#새로 접속하거나 새로고침했을때: get방식
#입력 폼을 작성하고 입력버튼 누르면 post방식
@app.route('/create/',methods=['GET','POST'])
def create():
    if request.method=='GET':    #method값이 get인지 post인지/ 아무것도 입력안하고 클릭하면 get나와서 화면 그대로
        in_put='''
        <form action='/create/' method='POST'>
            <p><input type="text" name='title' placeholder='title'></p>
            <p><textarea name='body' placeholder='body'></textarea></p>
            <p><input type='submit' value='입력'></p>
        </form>
        '''
        return template(getcontent(),in_put)      #입력값 없으면 나 자신으로
    elif request.method=='POST':   #입력하면 post방식으로 나오면서 실행
        global nextid        #함수안에서 쓰고 그 값이 영구히 바껴야하므로
        title=request.form['title']     #해당 name값에서 받은 데이터 변수에 저장
        body=request.form['body']
        newdata={'id':nextid,'title':title,'body':body} #입력받은 내용들을 딕셔너리형태로저장
        data.append(newdata)    #그 받은 새로운데이터를 기존 데이터에 더함
        url='/read/'+str(nextid)+'/'
        nextid=nextid+1              #입력될때마다 1씩증가
        return redirect(url)       #입력버튼 누르면 새로운 url로 이동


#여기가 첫페이지
@app.route('/')    
def index():       
    return template(getcontent(),'<h2>welcome</h2>hellow,WEB')


#여기는 정보들이 보여질 페이지
@app.route('/read/<int:id>/')  
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
