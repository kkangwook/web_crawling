### beautifulsoup
# pip install beautifulsoup4
# pip install lxml   (XML과 HTML문서를 파싱하고 처리->xpath를 이용해 특정 데이터 쉽게 선택)
import requests
from bs4 import BeautifulSoup

#네이버스포츠를 예제로
url='https://sports.news.naver.com/index.nhn'
res=requests.get(url)
res.raise_for_status()

soup=BeautifulSoup(res.text,'lxml') #  res.text를 lxml파서를 통해 beautifulsoup객체로 만듬

### 1.첫번째 태그 하나만 가져오기
# print()생략한것임
soup.title  # 결과: <title>네이버 웹툰</title>  ->title태그 가져옴
soup.title.get_text()  #결과: 네이버 웹툰  ->text는 태그 사이의 것

soup.a    # a태그는 여러개 존재하지만 제일 처음꺼 가져옴
soup.a.attrs # {속성: 속성값} 형태로 해당 첫번째 태그의 모든 데이터들 반환
# {'href': '#lnb_main_sub', 'onclick': "document.getElementById('lnb_main_sub').tabIndex=-1;document.getElementById('lnb_main_sub').focus();"}

soup.a['href'] #해당 속성의 속성 값만 가져옴
# #lnb_main_sub


### 2.페이지에 대해 잘 모를때 특이적으로 찾기
sf=soup.find('a',attrs={'href':'#lnb_main_sub'}) #-> a태그중 속성으로 'href':'#lnb_main_sub'가진 태그와 그 안의 정보들 가져오기

sf.span #저장된 a태그안에는 span태그도 존재-> span만 보기

#태그 지정없이 속성값만으로도 가능
sf1=soup.find(attrs={'href':'#lnb_main_sub'}) #이렇게도 가능(해당속성가져와조) but 중복되면 태그 이름도 지정

# 태그안의 text정보로 가져오기-> string=사용
match=soup.find('h2',string='오늘의 경기')
# 결과: <h2 class="blind">오늘의 경기</h2>



### 3. 여러개 가져오기 :find_all사용 ->리스트형태
# 예제1) 네이버 해외축구에서 모든 스포츠 팀명
url2='https://sports.news.naver.com/wfootball/index'
res2=requests.get(url2)
res2.raise_for_status()
soup2=BeautifulSoup(res2.text,'lxml')

#개발자도구 왼쪽 상단에 있는거 클릭 후 웹사이트화면에서 원하는 정보 클릭하면 해당 html구조로 이동
team=soup2.find_all('span',attrs={'class':'name'})  #span태그들 중 class:name속성 가진애들만
for i in team:           #리스트 형태이므로
    print(i.get_text())     #텍스트 가져오기

# 예제2) 축구 팀만 가져오기 
# 기존은 야구 팀등도 가져옴(class:name에 의해)
team=soup2.find_all('div',attrs={'class':'wrap'})  #축구칸으로 이동
for i in team:
    print(i.span.get_text())   #축구 칸 안에서 span의 text가져옴

team[0].span.get_text()   #리스트이므로 이렇게도 가능

# find 후에 find_all중복으로 사용가능
# 예제3) 분데스리가 팀만 가져오기
bundteam=soup2.find('div',attrs={'id':'_team_rank_bundesliga'}) #모든 리그는 class:wrap가지고 있어서 더 세부적인 id가져옴
team=bundteam.find_all('span',attrs={'class':'name'}) #그리고 이 안에서 span/ class:name사용하면 분데스리그특이적으로만 가져옴
for i in team:
    print(i.get_text())


# 예제4) 링크가져오기: 많이본 뉴스 첫번째 기사링크
news=soup2.find_all('span',attrs={'class':'number'})  #li에 id나 class가 없어 각li들밑의 공통된 span{class:number}가져옴
link=news[0].find_next_sibling('a')['href'] #여러 span들 중에 첫번째 span가져오고 링크값이 있는데 다음 형제인 a태그로 들어가 href속성 가져옴

for i in news:           #많이 본 뉴스 전부 가져오기
    print(i.find_next_sibling('a')['href'])
#링크는 ctrl+클릭하면 들어가짐


# 예제5) 해외축구 승점정보 가져오기
team=soup2.find_all('th',attrs={'scope':'row'})
for i in team:
    print(i.find_next_siblings('td')[5].get_text())  #th태그 형제들중 6번째 밑에 있는 td태그 텍스트 가져옴


# 예제6) 분데스리가 승점정보 가져오기
bundteam=soup2.find('div',attrs={'id':'_team_rank_bundesliga'})
team=bundteam.find_all('th',attrs={'scope':'row'})
for i in team:
    print(i.find_next_siblings('td')[5].get_text())  #6본째 td꺼


# find외에도 select, select_one이 있음
# 얘네들은 css의 요소들을 넣음

# a태그의 class 속성명이 news_tit인 태그 
soup.select_one('a.news_tit')  #첫번째거만

soup.select('a.news_tit')   #해당 전부가져옴


### 4.xpath사용하기
## <ul>밑에 여러 <li>들 존재

list1=soup.find('li',attrs={'class':'today_item'}) #첫번째 리스트

#밑의 형제
list1.next_sibling   #얘는 안나옴(아마 빈칸)
list2=list1.next_sibling.next_sibling  #얘는 나옴, 다음형제인 <li>가 나옴
list3= list2.next_sibling.next_sibling  #세번째 리스트

#next_sibling여러번 해야돼서 불편-> find_next_sibiling('조건') 사용
list2=list1.find_next_sibling('li') #다음형제중 li태그인애
list3=list2.find_next_sibling('li')

#형제들 한꺼번에 다가져오기
all_list=list1.find_next_siblings('li') #형제중 li인 애들만


#위의 형제
list2=list3.previous_sibling.previous_sibling  #세번째에서 그전인 두번째꺼 가져오기
# or
list2=list3.find_previous_sibling('li') #더 쉽게


#부모
parent=list1.parent  # <li>의 부모인 <ul>부터 시작해서 </ul>사이의 모든 정보(모든 <li>포함해서) 다겨져옴

