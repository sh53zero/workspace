
# 1.자료구조 복제
# copy란 객체의 주소를 복사하는 것.
# 얕은 복사: 객체의 주소를 그대로 넘겨주는 것.
# 깊은 복사: 객체의 내용만 넘겨주는 것.

# 1-1.얕은 복사: 주소 복사(내용, 주소 동일)
name=['홍길동','이순신','강감찬']
print('name address=', id(name))

name2=name  #주소 복사
print('name2 address=', id(name2))

print(name)  #['홍길동', '이순신', '강감찬']
print(name2)  #['홍길동', '이순신', '강감찬']

# 1-2.원본 수정
name2[0]='김길동'  #원본/사본 수정
print(name)  #['김길동', '이순신', '강감찬']
print(name2)  #['김길동', '이순신', '강감찬']

# 1-3.깊은 복사: 내용 복사(내용 동일, 주소 다름)
import copy
name3=copy.deepcopy(name)
print(name3)

print('name address=',id(name))
print('name3 address',id(name3))  #얕은 복사와는 다르게 주소가 다르게 나옴, 깊은 복사는 그냥 복사와는 다르게 같은 값이 아님

# 1-4.원본 수정
name[1]='이순신장군'
print(name)  #['김길동', '이순신장군', '강감찬']
print(name3)  #['김길동', '이순신', '강감찬']

