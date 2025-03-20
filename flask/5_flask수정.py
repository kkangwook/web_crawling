## 1. 수정
# 첫페이지에서 html, css, javascript중 하나의 링크를 타고 read페이지에 들어갔을때
# 수정을 눌러 해당 타이틀과, 바디를 바꾸기

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

#2. 여기 파라미터에도 id 추가
def template(list,content,id=None):   #첫페이지같은 경우에 id값 필요하지 않을수도 있어서
    contextui=''
    if id!=None:    #id가 있으면 contextui만들어짐->밑에 update링크 만들어짐
        contextui=f'''  
            <li><a href="/update/{id}/">update</a></li>'''
    return f'''<!doctype html>
    <html>
        <body>
            <h1><a href='/'>WEB</a><h1>
            <ol>
                {list}
            </ol>
            {content}
            <ul>
                <li><a href='/create/'>create</a></li>
                {contextui}
            </ul>
        </body>
    </html>
    '''    


nextid=4  




@app.route('/create/',methods=['GET','POST'])
def create():
    if request.method=='GET':   
        in_put='''
        <form action='/create/' method='POST'>
            <p><input type="text" name='title' placeholder='title'></p>
            <p><textarea name='body' placeholder='body'></textarea></p>
            <p><input type='submit' value='입력'></p>
        </form>
        '''
        return template(getcontent(),in_put)
    elif request.method=='POST':   
        global nextid        
        title=request.form['title']     
        body=request.form['body']
        newdata={'id':nextid,'title':title,'body':body} 
        data.append(newdata)    
        url='/read/'+str(nextid)+'/'
        nextid=nextid+1              
        return redirect(url)       

#3. update만들기(create와 비슷)
@app.route('/update/<int:id>/',methods=['GET','POST'])
def update(id):
    if request.method=='GET':
        title=''                    #값들 받아오기 위해
        body=''

        for i in data:
           if id==i['id']:
               title=i['title']
               body=i['body']
                 
        in_put=f'''
        <form action='/update/{id}/' method='POST'>
            <p><input type="text" name='title' placeholder='title' value="{title}"></p>
            <p><textarea name='body' placeholder='body'>{body}</textarea></p>
            <p><input type='submit' value='수정'></p>
        </form>
        '''
        return template(getcontent(),in_put)
    elif request.method=='POST':      #update에서 입력하면 post로
        global nextid        
        title=request.form['title']     
        body=request.form['body']
        for i in data:                  #이 값을 토대로 수정
            if id==i['id']:
                i['title']=title
                i['body']=body
                
#        newdata={'id':nextid,'title':title,'body':body} 
#        data.append(newdata)    
        url='/read/'+str(id)+'/'
                     
        return redirect(url)  


#여기가 첫페이지
@app.route('/')    
def index():       
    return template(getcontent(),'<h2>welcome</h2>hello,WEB</h2>')


#1. read에 id 추가
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
            break
    return template(data_lists,f'<h2>{body}</h2>',id)  #id추가
app.run(debug=True)

