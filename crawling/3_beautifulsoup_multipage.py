# url의 get방식과 post방식
#get: url에 정보들 있음 ex) ?minprice=1000&maxprice=10000&page=1
        # ?에서부터 변수를 의미, key=value형태, &으로 구분
# post: 페이지가 변해도 url은 그대로


# 쿠팡 예제(노트북 입력)-get방식, page=1로
import requests
import re
from bs4 import BeautifulSoup

url='https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page=1&rocketAll=false&searchIndexingToken=1=8&backgroundColor='
headers={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36'}
res=requests.get(url,headers=headers)
res.raise_for_status()

soup=BeautifulSoup(res.text,'lxml')

# 노트북의 이름 가져오기
pc=soup.find_all('li',attrs={'class':re.compile('^search-product')}) #search-product뒤에 추가로 붙은것도 있고 아닌것도 있어서 정규표현식 사용
pc1=pc[0].find('div',attrs={'class':'name'})
print(pc1)

#노트북 여러정보가져오기
for i in pc:
    name=i.find('div',attrs={'class':'name'}).get_text() #이름
    price=i.find('strong',attrs={'class':'price-value'}).get_text() #가격
    rate=i.find('em',attrs={'class':'rating'}) #평점-없을수도 있음
    if rate:
        rate=rate.get_text()
    else:
        rate='평점 없음'
    print(name,price,rate)

#광고상품 제거하기
for i in pc:
    ad=i.find('span',attrs={'class':'ad-badge-text'})
    if ad:
        continue      #생략하고 다음 i로
    name=i.find('div',attrs={'class':'name'}).get_text()
    print(name)

# 평점 4.5이상
for i in pc:
    name=i.find('div',attrs={'class':'name'}).get_text()
    rate=i.find('em',attrs={'class':'rating'}) 
    if float(rate)>=4.5:       #rate값은 str
        print(name, rate)

# 애플 제품 제거
if 'Apple' in name:
    continue


#여러페이지에서 (10페이지)
for i in range(1,11):
    url=f'https://www.coupang.com/np/search?page={i}&rocketAll=false' #page 1~10순차적으로 출력
    headers={'user-agent':'Mozilla/5.0~~~'}
    res=requests.get(url,headers=headers)
    res.raise_for_status()

    soup=BeautifulSoup(res.text,'lxml')
    pc=soup.find_all('li',attrs={'class':re.compile('^search-product')}) 
    print(f'{i}번째 페이지')
    for x in pc:
        name=x.find('div',attrs={'class':'name'}).get_text()
        price=x.find('strong',attrs={'class':'price-value'}).get_text() 
        rate=x.find('em',attrs={'class':'rating'}) 
        if rate:
            rate=rate.get_text()
        else:
            rate='평점 없음'
        link=x.find('a',attrs={'class':'search-product-link'})['href']
        print(name,price,rate)
        print(link)