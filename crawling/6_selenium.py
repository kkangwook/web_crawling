# pip install selenium
# 밑에껀 생략가능
    # 이후 webdriver다운->chrome driver
    # 주소창에 chrome://version으로 버전 확인
    # 검색창에 chrome driver치고 버젼에 맞게 다운

## 1.기본 작동
from selenium import webdriver
from selenium.webdriver.common.keys import Keys  #키보드 다룰 수 있게
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome()    #자동으로 크롬드라이버 실행

#웹툰 제목들 가져오기
driver.get('https://comic.naver.com/webtoon')   #사이트로 이동

#while True:        #자동 종료되지않게하기위해 무한루프
#    pass
time.sleep(3)     #로딩될때까지 기다림


### 찾는 함수들
#find_element(By.ID)
#find_element(By.CLASS_NAME)
#find_element(By.XPATH)
#find_element(By.CSS_SELECTOR)
#이 외에도 By.TAG_NAME(태그명으로ex)<p>,<div>), By.XPATH, By.NAME(name속성 사용), By.LINK_TEXT

#find_elements로 하면 리스트로 받아옴!!!!

title=driver.find_elements(By.CLASS_NAME,"text")

###값 가져오기->현재태그안의 값들만 가져옴!!!!

# 1-1. text가져오기: .text            
for i in title:
    text=i.text
    print(text)     #웹툰 제목들 출력

# 1-2. 속성값 가져오기: .get_attribute('속성값')

# 1-2-1. 각웹툰들 링크가져오기('href')
link=driver.find_elements(By.CLASS_NAME,"ContentTitle__title_area--x24vt")
for i in link:
    href = i.get_attribute('href')
    print(href)



# 1-2-2. 각 웹툰들 이미지 가져오기('src')/ ex)화산귀환
driver.get('https://comic.naver.com/webtoon/list?titleId=769209&tab=wed')   #사이트로 이동

time.sleep(3)
import requests    #src url가져올때
#user-agent있어야 제대로 저장가능/ 없으면 다운은 되는데 안에 내용이 없음
headers={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36'}

image1=driver.find_elements(By.CLASS_NAME,"EpisodeListList__thumbnail_area--EL1aw")
for idx, i in enumerate(image1):
    image2=i.find_element(By.TAG_NAME,'img')  #이미지 태그로 직접 이동해야 src가져올 수 있음
    url=image2.get_attribute('src')
    image_res=requests.get(url,headers=headers)

    with open(f'webtoon{idx+1}.jpg','wb') as f: # wb는 파일을 바이너리(2진수)모드로 쓸때
        f.write(image_res.content)   #content를 이진수형태의 데이터로 가져오며 f.write이 이를 이미지로 저장하게끔 함





####2. 자동화

#step1.검색할 키워드 입력
query = input('검색할 키워드를 입력하세요: ')

#step2.크롬드라이버로 원하는 url로 접속
url = 'https://www.naver.com/'
driver = webdriver.Chrome()
driver.get(url)
time.sleep(3)

#step3.검색창에 키워드 입력 후 엔터
search_box = driver.find_element(By.ID, "query") #검색창 id속성값이 query
search_box.send_keys(query)         #검색창에 query자동 입력
search_box.send_keys(Keys.RETURN)   #엔터->이동됨
time.sleep(2)

#step5.뉴스 탭 클릭
driver.find_element_by_xpath('//*[@id="lnb"]/div[1]/div/ul/li[2]/a').click()  #클릭
time.sleep(2)



###3. selenium과 beautifulsoup 함께사용!!!!
from bs4 import BeautifulSoup
# driver.page_source로 다가져옴
driver=webdriver.Chrome()    #자동으로 크롬드라이버 실행

driver.get('https://comic.naver.com/webtoon')   #사이트로 이동

time.sleep(3)

whole_page=driver.page_source  #다가져옴

with open('webtoon.html','w',encoding='utf-8-sig') as f:
    f.write(whole_page)

soup = BeautifulSoup(whole_page, 'lxml')