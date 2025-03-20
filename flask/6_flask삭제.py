# 삭제

from flask import Flask, request, redirect

app=Flask(__name__)

data=[
    {'id':1,'title':'html','body':'html is ...'},
    {'id':2,'title':'css','body':'css is ...'},
    {'id':3,'title':'javascript','body':'javascript is ...'}
]
nextid=4  


def getcontent():
    data_lists=''
    for i in data:      
        data_lists=data_lists+f'<li><a href="/read/{i["id"]}/">{i["title"]}</a></li>'     
    return data_lists

#1. 구조에 삭제버튼추가->링크 말고 버튼으로
def template(list,content,id=None):   
    contextui=''        #contextui에 delete 버튼 추가(submit, 안에 이름에 delete)
    if id!=None:                #submit클릭 시 delete/{id}로 이동, 만약 get방식이면 url치고 들어가자마자 삭제됨->post방식으로해서 방지
        contextui=f'''  
            <li><a href="/update/{id}/">update</a></li>
            <li><form action="/delete/{id}/" method="POST"><input type="submit" value="delete"></form></li>'''
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

#2. delete만들기
@app.route('/delete/<int:id>/',methods=['POST'])  #only post방식으로만
def delete(id):
    for i in data:
        if id==i['id']:
            data.remove(i)   #.remove로 리스트로된 데이터베이스에서 제거->바로 템플레이트 수준에서 부터 해당 데이터가 안나타남
            break
    return redirect('/')   #루트 페이지로 이동




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


@app.route('/update/<int:id>/',methods=['GET','POST'])
def update(id):
    if request.method=='GET':
        title=''                    
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
    elif request.method=='POST':     
        global nextid        
        title=request.form['title']     
        body=request.form['body']
        for i in data:                 
            if id==i['id']:
                i['title']=title
                i['body']=body
                
  
        url='/read/'+str(id)+'/'
                     
        return redirect(url)  



@app.route('/')    
def index():       
    return template(getcontent(),'<h2>welcome</h2>hello,WEB</h2>')



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
    return template(data_lists,f'<h2>{body}</h2>',id)  
app.run(debug=True)