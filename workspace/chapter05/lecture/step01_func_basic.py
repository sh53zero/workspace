
# 1.내장함수
# 1-1.builtins 함수
help(len)
dataset=list(range(1,6))
print(dataset)

print('len=',len(dataset))
print('sum=',sum(dataset))
print('max=',max(dataset))
print('min=',min(dataset))

# 1-2.import 함수
import statistics  #방법1
from statistics import variance, stdev  #방법2

print('평균=',statistics.mean(dataset))  #mean: 평균 / 방법1
print('중위수=', statistics.median(dataset))  #중위수 / 방법1
print('표본 분산=', variance(dataset)) #표본 분산 / 방법2
print('표본 표준편차=', stdev(dataset))  #표본 표준편차 / 방법2


# 2.사용자정의 함수
# 2-1.인수가 없는 함수
def userFunc1():
    print('인수가 없는 함수')
    print('userFunc1')

userFunc1()  #함수 호출

# 2-2.인수가 있는 함수
def userfunc2(x,y):
    print('userfunc2')
    z =x+y
    print('z=',z)
userfunc2(10,20)

# 2-3.return 있는 함수
def userfunc3(x,y):
    print('userfunc3')
    tot=x+y
    sub=x-y
    mul=x*y
    div=x/y

    return tot,sub,mul,div  #파이썬에서는 하나의 함수 안에 n가지의 실행문을 삽입 가능

# 실인수: 키보드 입력
x=int(input('x 입력:'))
y=int(input('y 입력:'))

t,s,m,d=userfunc3(x,y)  #파이썬에서는 순서대로 변수 삽입이 가능 (tot-t,sub-s,mul-m,div-d)
print('tot=',t)
print('sub=',s)
print('mul=',m)
print('div=',d)
