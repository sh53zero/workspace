
from bs4 import BeautifulSoup

#<처리 조건>
#1. <tr> 태그의 하위 태그인 <th>태그의 모든 내용 출력
#2. 각 단꼐 처리


# 1-1.파일 읽기
file=open('/chapter090/data/login.html', mode='r', encoding='utf-8')
source=file.read()  #파일 읽기 코드

# 1-2.html 파싱
html=BeautifulSoup(source,'html.parser')  #html 파싱
#print(html)

# 1-3.태그 찾기
trs=html.find_all('tr')  #tr태그의 하위태그라서 tr부터 셋팅
#print(trs)

# 1-4.태그 내용 출력
print('\nth tag 내용')
for tr in trs:  #tr 태그의 하위태그라서 tr in trs하고 그 안에 th 셋팅
    th=tr.find('th')
    print(th.string)