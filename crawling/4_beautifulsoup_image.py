# 이미지 불러오기
# 다음사이트에서 영화->역대관객순-> 연도별 영화이미지 가져오기
import requests
from bs4 import BeautifulSoup

url='https://search.daum.net/search?w=tot&q=2024%EB%85%84%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&DA=MOR&rtmaxcoll=MOR'
res=requests.get(url)
res.raise_for_status()

soup=BeautifulSoup(res.text,'lxml')

imgs = soup.find_all('a', attrs={'class': 'thumb_bf'})

for idx,image in enumerate(imgs):
    url=image.img['src']
    if 'https' not in url:
        continue
    image_res=requests.get(url)

    with open(f'movie{idx+1}.jpg','wb') as f: # wb는 파일을 바이너리(2진수)모드로 쓸때
        f.write(image_res.content)   #content를 이진수형태의 데이터로 가져오며 f.write이 이를 이미지로 저장하게끔 함

    

# 연도별 다가져오기
# url의 q=2024가 힌트-> 여기를 for i in range()해서 여러 페이지
for i in range(2024,2000,-1):
    url=f'https://search.daum.net/search?w=tot&q={i}%EB%85%84%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&DA=MOR&rtmaxcoll=MOR'
    res=requests.get(url)
    res.raise_for_status()

    soup=BeautifulSoup(res.text,'lxml')

    imgs = soup.find_all('a', attrs={'class': 'thumb_bf'})

    for idx,image in enumerate(imgs):
        url=image.img['src']
        if 'https' not in url:
            continue
        image_res=requests.get(url)

        with open(f'movie{i}_{idx+1}.jpg','wb') as f: # wb는 파일을 바이너리(2진수)모드로 쓸때
            f.write(image_res.content)