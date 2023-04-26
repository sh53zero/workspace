
# 모듈 import
import urllib.request as req
from bs4 import BeautifulSoup

# news 제공 포털 사이트
url='http://media.daum.net'

# 1-1.url 요청
res=req.urlopen(url)
source=res.read()

# 1-2.source 디코딩
source=source.decode('utf-8')  #charset='utf-8'

# 1-3.html 파싱
html=BeautifulSoup(source,'html.parser')

# 1-4.tab[속성-값] 요소 추출
atags=html.select('a[class=link_txt]')
print('a tag 수=',len(atags))

# 1-5.a 태그 내용 수집
crawling_data=[]  #빈 list

cnt=0
for atag in atags:
    cnt+=1
    atagStr=str(atag.string)  #string 변환
    crawling_data.append(atagStr.strip())
    '''
    string.strip():문단 끝 불용어(공백,tab,\n\r 제거
    '''

# 수집한 자료 확인
print('수집한 자료 확인')
print(crawling_data)

# 1-6.pickle save/load
import pickle  #project->file(binary)->load(object)

# save: binary file save
file=open('D:/git_office/workspace/chapter09/data/data.pickle',mode='wb')  #wb인 이유는 이진수로 저장해서
pickle.dump(crawling_data,file)

# load: binary file load
file=open('D:/git_office/workspace/chapter09/data/data.pickle',mode='rb')
crawling_data=pickle.load(file)
print('pickle load')
print(crawling_data)
