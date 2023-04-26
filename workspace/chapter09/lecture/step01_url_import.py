
# 1-1.request, BeautifulSoup 모듈 import
port urllib.request  #원격 서버 피일 요펑
from bs4 import BeautifulSoup

# 요청할 url
url='http://www.naver.com/index.html'

# 1-2.원격 서버 파일 요청
res=urllib.request.urlopen(url)  #web 문서
data=res.read()  #test 형태로 읽음

# 1-3.source 디코딩
src=data.decode('utf-8')  #디코딩
print(src)

# 1-4.html 파싱
html=BeautifulSoup(src,'html.parser')  #html 파싱
print(html)

# 1-5.태그내용
a=html.find('a')
print('a tag:',a)
print('a tag 내용:', a.string)