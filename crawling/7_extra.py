# 1. urllib 사용법 
from urllib.request import urlopen  # url요청, 읽기, 해독(한글) 
from bs4 import BeautifulSoup # html문서 파싱(문자열 -> html문서화 ) 


url = "http://www.naver.com/index.html"
 
# 1-1. 원격 서버 url 요청 
url_res = urlopen(url) # 요청 & 응답 
byte_data = url_res.read() # byte 읽기  

# 1-2. html 파싱 
text_data = byte_data.decode("utf-8") # 디코딩  

soup = BeautifulSoup(text_data, 'html.parser')

# 1-3. urllib로 이미지 다운
from urllib.request import urlretrieve

img_url=img.get('src')  # src형식(https:/~)의 url
urlretrieve(img_url, file_name)   #url과 파일이름 넣으면 됨
 -> request의 f.write(res.content)와 유사


# 1. requests에서 글자깨지면
res=requests.get(url,headers=headers)
res.encoding='utf-8'      #encoding해줌

# 2. 어떤 parser 사용?
1. 간단한 웹페이지 → html.parser
2. 속도 + 안정성 → lxml (가장 인기 많음)

# 3. find/find_all
기본형태는 find(tag,attrs={'name':'value'}
but
find(tag)
find(attrs={:})

추가로 a.get('href')와 a['href']는 같음

# 4. 선택자 사용
태그-> soup.select('p')
id-> soup.select_one('#tab')
id-> soup.select_one('a#tab')
class-> soup.select(".odd")
태그[속성='속성값'] -> soup.select("tr[class='odd']")

계층적 선택자 -> soup.select('#tab > tr > th')   단 >사용할꺼면 바로밑의 자손이어야함!!!!!!!!!!!!!!!!!!!
예시: html.select('div.news_view > div.article_view > section > p')
  -> div태그중 class로 news_view를 갖는애 밑의 div태그중 article_view라는 class를 가지는 태그 밑에 section태그 밑의 모든 p태그를 가져오겠다

좀떨어져 있는 자손 찾을때->
soup.select('#tab > tr > th') 대신 soup.select('#tab th')가능!!!!!!!!!


--------------------------------------------------------------------------------------------------------------------
from selenium import webdriver # driver 
from selenium.webdriver.chrome.service import Service # Chrom 서비스
from webdriver_manager.chrome import ChromeDriverManager # 크롬드라이버 관리자  
from selenium.webdriver.common.by import By # 로케이터
from selenium.webdriver.common.keys import Keys
import os
import time # 화면 일시 정지 

# 1. 크롬 driver 생성 
driver_path = ChromeDriverManager().install() # 드라이버 설치 경로 
correct_driver_path = os.path.join(os.path.dirname(driver_path), "chromedriver.exe") # 실행파일경로 
driver = webdriver.Chrome(service=Service(executable_path=correct_driver_path)) # 드라이버 생성 


# 2. 대상 url 이동 
driver.get('https://www.naver.com/')




1. selenium find_element   ->class_name, id외
driver.find_element(By.NAME, 'name이름') # name 속성으로 찾기

driver.find_element(By.TAG_NAME, 'p') # tag 이름으로 찾기

driver.find_element(By.XPATH, 'xpath') # 절대경로 or 상대경로로 찾기
login=driver.find_element(By.XPATH,'//*[@id="account"]/div/a') #우클릭->복사->xpath복붙

driver.find_element(By.LINK_TEXT,'텍스트')  # a태그안의 .text
driver.find_element(By.LINK_TEXT,'경제')  #경제라는 텍스트와 링크를 가지면 가져올수있음->애매할때가 많아 잘 사용 X

driver.find_element(By.CSS_SELECTOR, ‘CSS선택자이름’) # 선택자로 찾기
driver.find_element(By.CSS_SELECTOR,'#account > div > a')  #우클릭->복사->selector복사
f12후 select버튼 누르고 갔다대면 맨 위에 나오는게 css_selector








2. selenium 버튼
from selenium.webdriver.common.keys import Keys


driver.get('https://www.naver.com/')
query_btn = driver.find_element(By.ID,'search-btn')   #검색버튼
query=driver.find_element(By.ID,'query')      #검색창
query.send_keys('안녕')            #검색문 입력

-엔터하고 싶으면 둘 중 하나
query.send_keys(Keys.ENTER)
login_btn.click() # 로그인 버튼 클릭 
time.sleep(2) # 2초 일시 중지 

driver.back() # 현재페이지 -> 뒤로
time.sleep(2) # 2초 일시 중지 
  
driver.forward() # 현재페이지 -> 앞으로 
driver.refresh() # 페이지 새로고침(F5)
time.sleep(2) # 2초 일시 중지 

driver.close() # 현재 창 닫기 


네이버 같은데에 입력하고싶을때
input_url=f"https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query={input}"


3. 로봇이 아닙니다
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument('--disable-blink-features=AutomationControlled')
driver = webdriver.Chrome(options=options)


4. 검색 후 찾기
주의!!!->처음 driver.get이후 이 url은 send_key나 click을 통해 그 값이 계속 바뀌기 때문에 driver를 고쳐줄 필요없이
그냥 옮겨진화면에서 driver.find_element하면됨
단 새창이 열리는게 아닌 기존 창을 계속유지해야함!!!!!!!!

예시)
driver.get('https://www.naver.com/') # url 이동 
time.sleep(3)
cafe=driver.find_element(By.LINK_TEXT,'카페')
driver.execute_script("arguments[0].removeAttribute('target')", cafe)  이과정이 중요!!!!!
cafe.click()
time.sleep(3)

hot=driver.find_element(By.XPATH,'//*[@id="gnbMenu"]/a[4]')   #그대로 사용가능
hot.click()
time.sleep(3)
toptext=driver.find_elements(By.CLASS_NAME,'tit')    #그대로 사용기능
for i in toptext:
    print(i.text)
print(len(toptext))
driver.close()


5. 안나오는 이미지 src찾기
url = f"https://search.naver.com/search.naver?query={query}" # 기본 url 
    
driver.get(url) # url 이동  
time.sleep(2) # 3초 대기 
    
    
# 3. [이미지] 링크 클릭 -> 이미지 검색 페이지 이동  
image_tab=driver.find_element(By.XPATH,'//*[@id="lnb"]/div[1]/div/div[1]/div/div[1]/div[1]/a')
image_tab.click()
    
    
# 4. 이미지 10개 수집         
time.sleep(5)  
for i in range(1,11):         xpath f''로 해서 가져오기!!!!1
    image=driver.find_element(By.XPATH,f'//*[@id="main_pack"]/section/div[1]/div/div/div[1]/div[{i}]/div/div/div/img')
    print(image.get_attribute('src'))

각 그림에 대한 xpath찾은방법
-> 하나씩 다 뽑아봐서 딱하나 차이나는것을 찾음
'''
//*[@id="main_pack"]/section/div[1]/div/div/div[1]/div[1]/div/div/div/img
//*[@id="main_pack"]/section/div[1]/div/div/div[1]/div[2]/div/div/div/img
//*[@id="main_pack"]/section/div[1]/div/div/div[1]/div[3]/div/div/div/img
'''




6. 함수만들기
def googleSearch(searchword):
    driver_path = ChromeDriverManager().install() # 드라이버 설치 경로 
    correct_driver_path = os.path.join(os.path.dirname(driver_path), "chromedriver.exe") # 실행파일경로 
    #driver = webdriver.Chrome(service=Service(executable_path=correct_driver_path)) # 드라이버 생성 

    # '로봇이 아닙니다' 라는 메시지가 나오는 경우
    options = Options()
    options.add_argument('--disable-blink-features=AutomationControlled')
    driver = webdriver.Chrome(options=options)

    # 2. url 이동 : 구글 페이지 이동 
    driver.get("https://www.google.com/") # 구글 페이지 이동
    box=driver.find_element(By.NAME,'q')
    box.send_keys(i)
    box.send_keys(Keys.ENTER)
    time.sleep(3)
    h3=driver.find_elements(By.TAG_NAME,'h3')
    list=[i.text for i in h3]
    driver.close()
    return list
searchword_list = ['머신러닝','통게분석','SQL']
for i in searchword_list:
    print(googleSearch(i))


7. 화면 스크롤바를 내려야 할수도 있음
last_height = driver.execute_script("return document.body.scrollHeight") #현재 스크롤 높이 계산

while True: # 무한반복
    # 브라우저 끝까지 스크롤바 내리기
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") 
    
    time.sleep(2) # 2초 대기 - 화면 스크롤 확인

    # 화면 갱신된 화면의 스크롤 높이 계산
    new_height = driver.execute_script("return document.body.scrollHeight")

    # 새로 계산한 스크롤 높이와 같으면 stop
    if new_height == last_height: 
        break
    last_height = new_height # 새로 계산한 스크롤 높이로 대체 
