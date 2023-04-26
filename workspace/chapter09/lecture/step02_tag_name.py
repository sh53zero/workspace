
from bs4 import BeautifulSoup
# 1-1.로컬 서버 파일 읽기
file= open('/chapter090/data/html01.html', mode='r', encoding='utf-8')
text=file.read()

# 1-2.html 파싱
html=BeautifulSoup(text,'html.parser')

# 1-3.태그 내용 가져오기
# tag 이용
h1=html.html.body.h1  #계층 접근
print('h1:', h1.string)

# find('tag')함수
h2=html.find('h2')
print('h2:',h2.string)

# find_all('tag') 함수
lis=html.find_all('li')
print(lis)

# li 태그 내용
for li in lis:
    print(li.string)