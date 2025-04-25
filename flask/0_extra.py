-남들이 들어올 수 있는 사이트 만들기
app.run(host='192.168.16.5', port=3179)
# http://192.168.16.5:3179/  남들이 치면 들어올 수 있음

---render template사용법---
html파일은 항상 templates폴더 안에->위치 지정시 templates는 쓸 필요 X
from flask import Flask, render_template
-기본
@app.route("/") 
def index() : # 응답 함수 
    return render_template('/step01/main.html') #templates안에 step01폴더안에 main.html을 가져오겠다

-이미지 가져오기
해당 html에
<img src="{{ url_for('static', filename='images/ai.jpg') }}"/> 
# .py가 있는 위치에서 static=폴더위치 filename=그 폴더 안에서부터 디렉토리/파일명

-링크 이동
@app.route("/") 
def index() : # 응답 함수 
    return render_template('/step01/main.html')  

@app.route('/cont') 
def info() : # 응답 함수
    return render_template('/step01/cont.html') 
/cont로 이동 위해 main.html에 <a href='/cont'> cont로 이동</a> 서식이 존재
-> app.route(위치)에서 href=위치  하면 됌
