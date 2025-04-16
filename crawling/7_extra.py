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

계층적 선택자 -> soup.select('#tab > tr > th')
예시: html.select('div.news_view > div.article_view > section > p')
  -> div태그중 class로 news_view를 갖는애 밑의 div태그중 article_view라는 class를 가지는 태그 밑에 section태그 밑의 모든 p태그를 가져오겠다
