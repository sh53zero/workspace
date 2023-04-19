
# 특수함수
# 1.가변인수  /  def 함수명 (매개변수, *매개변수, **매개변수):
# 1-1.튜플형 가변인수
def Func1(name, *names):
    print(name)  #홍길동
    print(names)  #('이순신','유관순')

Func1('홍길동','이순신','유관순')

# 1-2.통계량 구하는 함수
#statistics 모듈 import
from statistics import mean, variance, stdev
def statis(func, *data):  #가변인수를 활용해서 function과 data를 입력하여 값 출력하는 함수
    if func=='avg':  #평균
        return mean(data)
    elif func=='var':  #분산
        return variance(data)
    elif func=='std':  #표준편차
        return stdev(data)
    else:
        return 'TypeError'

#statis 함수 호출
print('avg=', statis('avg',1,2,3,4,5))
print('var=', statis('var',1,2,3,4,5))
print('std=', statis('std',1,2,3,4,5))

# 1-3.dict형 가변인수 / key와 value가 있는 함수
def emp_func(name,age,**other):
    print(name)
    print(age)
    print(other)  #{'addr': '서울시', 'height': 175, 'weight': 65} / dict는 {key, value},

# emp_func 함수 호출
emp_func('홍길동',35,addr='서울시',height=175,weight=65)


# 2.람다함수
# 정의와 호출을 한번에 하는 익명함수
# (lambda 매개변수: 실행문)(반환값)
# 2-1.일반 함수
def Adder(x,y):
    add=x+y
    return add

print('add',Adder(10,20))

# 2-2.위 일반 함수를 람다 함수로 변경
print('add=',(lambda x,y:x+y)(10,20))  #(lambda 매개변수x,매개변수y:실행문)(value)


# 3.스코프
# 변수가 사용되는 범위를 스코프라고 한다.
# def 함수명(인수): global 전역변수
# 3-1.지역변수 예
x=50  #전역변수 / def 밖에다 지정해서 전역변수가 됨
def local_func(x):
    x+=50  #지역변수 -> 종료 시점 소멸 / def 내에 지정해서 지역변수가 됨
local_func(x)
print('x=',x)  #x=50

# 3-2.전역변수 예
def global_func():
    global x  #전역변수 x 사용
    x+=50  #x+50=100 (x가 50이라 50+50=100=x가 됨)
global_func()
print('x=',x)  #x=100

