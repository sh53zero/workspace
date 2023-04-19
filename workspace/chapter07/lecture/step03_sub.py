
# 문자열 치환
from re import sub

st3='test^홍길동 abc 대한*민국 123$tbc'

# 1-1.특수문자 제거
text1=sub('[\^*$]+','',st3)
print(text1)  #test홍길동 abc 대한민국 123tbc / 특수문자를 공백으로 치환하여 특수문자 제거

# 1-2.숫자 제거
text2=sub('[0-9]','',text1)
print(text2)  #test홍길동 abc 대한민국 tbc / 숫자를 공백으로 치환하여 숫자 제거

# 1-3.한글 제거
text3=sub('[가-힣]','',text1)
print(text3)  #test abc  123tbc / 한글을 공백으로 치환하여 한글 제거

# 1-4.영문 제거
text4=sub('[a-z|A-Z]','',text1)
print(text4)  #홍길동  대한민국 123 / 영문을 공백으로 치환하여 영문 제거