# 부모-자식(자식끼리는 형제)

### 1. xpath:  원하는 곳으로 이동
# 원래: /학교/학년/반/학생[2] ex) /html/body/div/span/a..

#/html/body/div[2]/div[2]/div[2]/div[2]/div/div/div[1]/div/a
# ㄴ xpath이용시-> //*[@id="account"]/div/a
# /하나는 현재에서 한단계 아래, //는 현재에서 아래의 모든단계 전체를 보겠다
# *는 모든 태그, or 원래는 *대신 태그넣어서 찾음
# @는 속성값, id는 내가 명명해준것
# 해석: 모든 태그에서 account id값 갖은애의 태그밑의 div태그 밑의 a태그를 가져오겠다

# 크롬에서 웹상 html위치 보기
## 해당 부분 우클릭 후 검사클릭->개발자도구열리고 위치뜸



### 2. requests
# pip install requests
import requests
# 페이지 정보 가져오기
res=requests.get('https://www.naver.com/')

# 제대로 가져왔는지 확인
print(res.status_code)  # 200뜨면 정상, 403이면 접근할 권한이 없음을 의미->다른 방법 사용
# 이때 requesets.codes.ok는 값이 200
#하지만 주로 위의 res=req~와 함께 밑에 코드 붙여씀
res.raise_for_status() #오류나면 바로 중지

# print(res.text) -> 정보가져옴(엄청많음)
print(len(res.text))

# 받은 텍스트 html파일로->우클릭 후 open in defualt browser로 열음
# with open('mynaver.html','w',encoding='utf-8') as f:
#      f.write(res.text)



### 3.정규식으로 글자가져옴
#import re하고 p=re.compile('찾을글자') :얘가 기준
# m=p.match('데이터') ->맨 앞에서부터 매치되는것 가져옴
# m.group() -> 매치된 값 반환 

# m=p.search('데이터') ->전체중에 맞는 부분 가져옴
# m.group()
# m.string ->입력받은 문자열(데이터) 출력
# m.start() or m.end() -> 일치하는 문자 index
# m.span() ->일치하는 문자 시작과 끝

# p.findall('데이터')  ->일치하는 모든것을 리스트 형태로



### 4. user agent: resquests.get했을때 오류나는 것을 해결
# user가 아닌 컴퓨터가 접속한다하면 강제적으로 막아서 발생
url='https://nadocoding.tistory.com/'
res=requests.get(url) #오류난다 가정
res.raise_for_status()
print('nodocoding:',res.status_code)

# with open('nadocoding.html','w',encoding='utf-8') as f:
#    f.write(res.text)

### 해결방법
## 구글에 user agent string치고-> whatismybrowser.com들어감->맨 위에 파란부분이 나의 정보->복붙
# Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36

headers={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36'}
res=requests.get(url,headers=headers)
res.raise_for_status()
print('nodocoding:',res.status_code)

with open('nadocoding.html','w',encoding='utf-8') as f:
   f.write(res.text)