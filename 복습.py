# webcrawling
1. beautifulsoup의 find로 축구팀 리스트 가져오기
2. beautifulsoup의 select로 계층적 선택자 이용해 한번에 탑뉴스리스트 전부->여기서 링크 추출
3. beautifulsoup으로 1~10페이지의 극내 시총 주식정보 스크래핑 후 csv로 저장
4. selenium으로 query입력받은 다음 네이버 홈페이지에 입력 후 이동->뒤로->앞으로->새로고침-> 이미지로 이동 후 상단 10개 이미지 저장하기


# flask
1. 홈페이지 제작-> 탭에 myhomepage, 화면에 큰 'homepage'링크텍스트(클릭하면 그대로 홈페이지로), html~css~javascript링크, create링크 , 'db로 이동' 링크
2. html~css~javascript클릭하면 body로 이동하며 title과 밑에 내용있음, create링크, update링크, delete링크, db로 이동 링크
3. create flask생성 -> text와 textarea로 입력받아 새로운 데이터 생성
4. update flask생성 -> text와 textarea로 입력받아 기존 데이터 변경
5. delete flask생성 -> 버튼으로 입력받아 클릭하면 해당 데이터 삭제
6. db로 이동 링크 클릭하면 로그인 창 뜸 -> user='c##scott',password='tiger' ->제대로 되면 db로/ 잘못되면 '잘못된 계정' 출력후 홈페이지와 로그인 링크 두 종류 제공
7. db로 이동 시 select입력으로 emp의 ename값과 보고싶은 열 데이터 두가지 입력받음->클릭시 해당 데이터 보여줌
