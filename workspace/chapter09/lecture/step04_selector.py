
from bs4 import BeautifulSoup

# 1-1.로컬 파일 읽기
file=open('/chapter090/data/html03.html', mode='r', encoding='utf-8')
source=file.read()

# 1-2.html 파싱
html=BeautifulSoup(source, 'html.parser')

# 1-3.선택자 이용 태그 내용 가져오기
# id-'tab'선택자
print('>>table 선택자')
table=html.select_one('#tab')
print(table)

# id 선택자와 계층
print('>>선택자 &계층<<')
ths=html.select('#tab>tr>th')
print(ths)  #list

# class 선택자: tr tag class='odd'
trs=html.select('#tab>.odd')  #홀수행
print('>>class 선택자<<')
print(trs)

# 1-4.태그[속성=값] 찾기
trs=html.select('tr[class=odd]')

# 1-5.td 태그 사용
print('>>tr>td출력<<')
for tr in trs:  #행:2회 반복
    tds=tr.find_all('td')
    for td in tds:  #열
        print(td.string)

        