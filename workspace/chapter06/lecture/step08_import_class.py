
# 내장클래스
# 1-1.리스트 열거형 객체 이용

lst=[1,3,5]
for i, c in enumerate(lst):  #인덱스는 0부터 시작함 / c는 값을 받는 변수임
    print('색인:',i,end=',')
    print('내용:',c)
    #색인: 0, 내용: 1
    #색인: 1, 내용: 3
    #색인: 2, 내용: 5

# 1-2.튜플 열거형 객체 이용
dit={'name':'홍길동','job':'회사원','addr':'서울시'}
for i, k in enumerate(dit):
    print('순서:',i,end=',')  #순서: 0,순서: 1,순서: 2,
    print('키:',k,end=',')  #키: name,키:job,키:addr
    print('값:',dit[k])  #값:홍길동, 값:회사원, 값:서울시
    #순서: 0, 키: name, 값: 홍길동
    #순서: 1, 키: job, 값: 회사원
    #순서: 2, 키: addr, 값: 서울시


# 2-1.모듈 내장클래스 import
import datetime  #모듈 import
from datetime import date, time

# 2-2.date 클래스
help(date)

today=date(2019,10,23)  #date 객체 생성
print(today)  #2019-10-23

# date 객체 멤버변수 호출
print(today.year)  #2019
print(today.month)  #10
print(today.day)  #23

# date 객체 멤버변수 호출
w=today.weekday()
print('요일 정보:',w)  #요일 정보: 2 / (수요일)

# 2-3.time 클래스
help(time)

currTime=time(21,4,30)  #time 객체 생성
print(currTime)  #21:04:30 / time 객체 정보

# time 객체 멤버변수 호출
print(currTime.hour)  #21
print(currTime.minute)  #4
print(currTime.second)  #30

# time 객체 메서드 호출
isoTime=currTime.isoformat()  #HH:MM:SS
print(isoTime)  #21:04:30

