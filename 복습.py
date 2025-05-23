from selenium.webdriver.support.ui import WebDriverWait 하고
element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/section/section/main/div/form/div/span/input'))) 하면 해당 구조가 나올때까지 기다렸다가 구조가져옴 (find_element와 유사)
-박스에 입력문넣어 enter하는 경우 .back으로 돌아가 다시 입력하려면 box.clear()가 반드시 필요



# webcrawling
1. beautifulsoup의 find로 축구팀 리스트 가져오기
2. beautifulsoup의 select로 계층적 선택자 이용해 한번에 탑뉴스리스트 전부->여기서 링크 추출
3. beautifulsoup으로 1~10페이지의 극내 시총 주식정보 스크래핑 후 csv로 저장
4. selenium으로 query입력받은 다음 네이버 홈페이지에 입력 후 이동->뒤로->앞으로->새로고침-> 이미지로 이동 후 상단 10개 이미지 저장하기


# flask
- itwill/textmining/workspace/flask의 flask_practice.py에 작성
1. 홈페이지 제작-> 탭에 myhomepage, 화면에 큰 'homepage'링크텍스트(클릭하면 그대로 홈페이지로), html~css~javascript링크, create링크 , 'db로 이동' 링크
2. html~css~javascript클릭하면 body로 이동하며 title과 밑에 내용있음, create링크, update링크, delete링크, db로 이동 링크
3. create flask생성 -> text와 textarea로 입력받아 새로운 데이터 생성
4. update flask생성 -> text와 textarea로 입력받아 기존 데이터 변경
5. delete flask생성 -> 버튼으로 입력받아 클릭하면 해당 데이터 삭제
6. db로 이동 링크 클릭하면 로그인 창 뜸 -> user='scott',password='tiger' ->제대로 되면 /database/로 잘못되면 /error/ '잘못된 계정' 출력후 홈페이지와 로그인 링크 두 종류 제공
7. /database/로 이동 시 select입력으로 emp의 ename값을 입력->클릭시 /emp/로 이동
8. 이 /emp/는 templates안의 practice.html로 불러와 jinja2형식 사용-> for문과 if문 사용해 입력받은 이름은 'ename의 월급은 sal원입니다 볼드체로 출력'
->그 밑에 static/images에서 홍길동 사진 가져옴-> 그 외의 선택받지 않은 ename들은 '누군가의 월급은 sal원'으로 리스트로 모두 출력
->다른정보보기 링크로 /database/로 이동하는 링크 생성
-> app.py에서는 session간단하게 사용해보기 (app.secret_key = '임의의_비밀키') 작성 필요
