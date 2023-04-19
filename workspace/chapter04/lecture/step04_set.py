
# 비순서 자료구조
# set: 원소들의 집합
# dict: key와 value의 집합

# 1.set {}
# 비순서 자료구조를 갖는 열거형객체를 생성할 수 있다.
# {} 안에 ,를 이용하여 원소 구붐
# 변수={값1, 값2, ... , 값n}
# 중복 허용하지 않음 (tuple, list에서는 중복 허용함)
# 순서가 없기 때문에 색인-index- 사용 불가.
# 객체에서 제공하는 함수를 이용하여 추가, 삭제 및 집합 연산 등이 가능.

# 1-1.셋 객체 예
# 중복 불가
s={1,3,5,3,1}
print(len(s))  #3
print(s)  #{1,3,5}

#
for d in s:
    print(d,end="")  #{1,3,5}
print()

# 집합관련 합수
s2={3,6}
print(s.union(s2))  #합집합 (union) / {1,3,5,6}
print(s.difference(s2))  #차집합 (difference) / {1,5}
print(s2.difference(s))  #차집합 (difference) / {6}
print(s.intersection(s2))  #교집합 (intersection) / {3}

# 추가, 삭제 함수
s3={1,3,5}
print(s3)
s3.add(7)  #원소 추가
print(s3)  #{1,3,5,7}
s3.discard(3)  #원소 삭제
print(s3)  #{1,5,7}

# 1-2.중복 제거
# 붕복을 허용하지 않는 set의 특징을 이용하여 list의 중복 원소를 제거하는데 set 이용 가능.
# 중복 원소를 갖는 list
gender=['남','여','남','여']

# 중복 원소 제거
sgender=set(gender)  #list->set / {'남','여'}
print(sgender)
lgender=list(sgender)  #set->list ['남','여']
print(lgender)  #['남','여']
print(lgender[1])  #'여'

