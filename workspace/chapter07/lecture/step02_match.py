
# 문자열 검사
from re import match  #re 모듈 import
# 1-1.패턴과 일치된 경우
jumin='123456-3234567'
result=match('[0-9]{6}-[1-4][0-9]{6}',jumin)
print(result)  #<re.Match object; span=(0, 14), match='123456-3234567'> / matching 안될 경우 None으로 출력

if result:  #object
    print('주민번호 일치')

else: #null
    print('잘못된 주민번호')

# 1-2.패턴과 불일치된 경우
jumin='123456-5234567'
result=match('[0-9]{6}-[1-4][0-9]{6}',jumin)
print(result)  #None

if result:  # object
    print('주민번호 일치')

else:  # null
    print('잘못된 주민번호')
