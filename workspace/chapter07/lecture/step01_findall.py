
# 문자열 찾기
import re #모듈 추가 - 방법1
from re import findall  #모듈 추가 - 방법2

stl='1234 abc홍길동 ABC_555_6 이사도시'

# 1-1.숫자 찾기
print(findall('1234',stl))  #['1234']
print(findall('[0-9]',stl))  #['1', '2', '3', '4', '5', '5', '5', '6'] / []안에서 0부터 9 숫자를 찾아라
print(findall('[0-9]{3}',stl))  #['123', '555'] / [숫자]안에서 세 글자 반복되는 것을 찾아라
print(findall('[0-9]{3,}',stl))  #['1234', '555'] / [숫자]안에서 세 글자이상 반복되는 것을 찾아라
print(findall('\\d{3,}',stl))  #['1234', '555'] / [숫자]안에서 ??

# 1-2.문자열 찾기
print(findall('[가-힣]{3,}',stl))  #['홍길동', '이사도시'] / [한글]안에서 세 글자이상 반복되는 첫을 찾아라
print(findall('[a-z]{3}',stl))  #['abc'] / [소문자알파벳]안에서 세 글자 반복되는 것을 찾아라
print(findall('[a-z|A-Z]{3}',stl))  #['abc', 'ABC'] / [소문자|대문자알파벳]안에서 세 글자 반복되는 것을 찾아라

# 1-3.특정 위치의 문자열 찾기
# 접두어 접미어
st2='test1abcABC 123mbc 45test'
print(findall('^test',st2))  #['test'] / 접두어-test로 시작하는 것 찾아라
print(findall('st$',st2))  #['st'] / 접미어-st로 시작하는 것 찾기

# 종료 문자 찾기: abc, mbc
print(findall('.bc',st2))  #['abc', 'mbc'] / bc로 끝나는 단어 찾기 (점 갯수에 따라 앞 문자 추가됨)

# 시작 문자 찾기
print(findall('t..',st2))  #['tes', 't1a', 'tes']/ t로 시작하는 문자 찾기 (점 갯수에 따라 뒷 문자 추가됨)

# 1-4.단어 찾기(\\w) - 한글+영문+숫자
st3='test^홍길동 abc 대한*민국 123$tbc'
words=findall('\\w{3,}',st3)
print(words)  #['test', '홍길동', 'abc', '123', 'tbc'] / 3글자 이상 단어 찾기

# 1-5.문자열 제외:x+(x가 1개 이상 반복)
print(findall('[^^*$]+',st3))  #['test', '홍길동 abc 대한', '민국 123', 'tbc'] / ^,*,$ 제외한 단어 찾기

