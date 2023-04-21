
from bs4 import BeautifulSoup  #html vktld

# 1-1.로컬 파일 읽기
file=open('D:/git_office/workspace/chapter09/data/html02.html', mode='r', encoding='utf-8')
source=file.read()

# 1-2.html 파싱
html=BeautifulSoup(source, 'html.parser')

# 1-3.a 태그 찾기
links=html.find_all('a')  #list 반환
print('links size=', len(links))

# 1-4.a태그에서 속성 찾기
for link in links:
    try:
        print(link.attrs['href'])
        print(link.attrs['target'])
    except Exception as e:
        print('예외 발생:',e)

# 1-5정규표현식으로 속성 찾기
import re
print('패턴 객체 이용 속성 찾기')
patt=re.compile('http://')  #patter object 생성
links=html.find_all(href=patt)  #패턴 찾기
print(links)
