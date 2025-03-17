# 네이버 금융정보 csv로 저장->코스피 시가총액 순위 검색->더보기
import requests
from bs4 import BeautifulSoup
import csv


filename='시가총액.csv'   #미리 파일만듬
f=open(filename,'w',encoding='utf-8-sig',newline='') #newline공백으로 해서 줄 사이사이에 공백줄있는거 없앰, 파일생성
writer=csv.writer(f) # f파일에 csv로 저장할수있게하는 객체를 생성
title='N	종목명	현재가	전일비	등락률	액면가	시가총액	상장주식수	외국인비율	거래량	PER	ROE	토론실'.split('\t')
writer.writerow(title)  #처음에 컬럼명에 title값 집어넣음, 리스트 각 요소가 각 속성값에 들어감

for i in range(1,11):
    url=f'https://finance.naver.com/sise/sise_market_sum.nhn?sosok=0&page={i}'
    res=requests.get(url)
    res.raise_for_status()

    soup=BeautifulSoup(res.text,'lxml')

    stock=soup.find('table',attrs={'class':'type_2'}).find('tbody').find_all('tr')
    for row in stock:
        columns=row.find_all('td')
        if len(columns)<=1:  #의미없는 데이터 제거
            continue
        data=[column.get_text() for column in columns] #한줄에 있는 td값들 하나의 리스트에 저장
        #print(data)
        writer.writerow(data)   #만들어둔 writer객체에 data(리스트)를 줄마다 삽입
