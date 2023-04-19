
# 딕트(dict)
# dict는 사정형으로 여러 개의 자료를 비순서로 적재하는 가변 길이 비순차 자료구조를 생성하는 클래스.
# set와의 차이점은 key와 value가 존재함

# 1-1.딕트 객체 특징
# 변수={'키':'값', '키':'값', ... '키':'값'}
# key는 중복이 허용되지 않고, value는 중복이 허용된다.
# index 대신에 key를 이용해서 value를 참조한다.
# key를 색인으로 이용할 수 있기 때문에 원소 수정, 삭제, 추가 등이 가능하다.
# !!색인이 있는 list도 원소 수정 등이 가능했음. set은 색인이 없어서 불가능.

# dict 생성 방법1
dic=dict(key1=100, key2=200, key3=300)
print(dic)  #{'key1':100, 'key2':200, 'key3':300}

# dict 생성 방법2
person={'name':'홍길동','age':'35','adress':'서울시'}
print(person)  #{'name': '홍길동', 'age': '35', 'adress': '서울시'}
print(person['name'])  #홍길동
print(type(dic),type(person))  #<class 'dict'> <class 'dict'>

# dict 원소 수정
person['age']=45  #변경하고 싶은 항목을 n['i']=d 형식으로 수정
print(person)  #{'name': '홍길동', 'age': 45, 'adress': '서울시'}

# dict 원소 삭제
del person['adress']
print(person)  #{'name': '홍길동', 'age': 45}

# dict 원소 추가
person['pay']=350
print(person)  #{'name': '홍길동', 'age': 45, 'pay': 350}


# 2.요소 검사와 반복
# dict는 set과 같이 비순서 자료구조이지만 열거형 객체이기 떄문에 요소 검사와 요소 반복 기능을 지원한다.
# 2-1.요소 검사
print(person['age'])  #45 / print(dict['i']) < key에 해당하는 value 찾기
print('age' in person)  #True / print('i' in dict) <key의 존재여부
print('adress' in person)  #False

# 2-2.요소 반복 !! data분석에서 가장 많이 쓰임!!
for key in person.keys():  #key 출력 / name age pay
    print(key)
for v in person.values():  #value 출력 / 홍길동 45 350
    print(v)
for i in person.items():  #key와 value를 같이 출력 / ('name', '홍길동') ('age', 45) ('pay', 350)
    print(i)


# 3.단어 빈도수 구하기
# 3-1.단어 데이터 set
charset=['abc','code','band','band','abc']
wc={}  #빈 set

# 3-2.get()함수 이용
for key in charset:
    wc[key]=wc.get(key,0)+1  #abc:2, code:1, band:2
print(wc)  #{'abc': 2, 'code': 1, 'band': 2}


