
# 중첩함수
# 함수 내부에 또 다른 함수가 내장된 형태.
# 내부 함수를 포함하는 함수를 외부 함수
# def 외부함수(인수):
#     실행문
#     def 내부함수(인수):
#         실행문
#         return 값
#     return 내부함수

# 1.일급함수
# 중첩함수는 외부함수나 내부함수를 변수에 저장할 수 있는데, 이러한 특성을 갖는 함수가 일급함수.
# 내부함수는 외부함수의 return 명령문을 이용하여 반환하는 형태를 함수 클로저(function cloure)라고 한ㅁ.
# 1-1.
def a():  #outer
    print('a 함수')
    def b():  #inner
        print('b 함수')
    return b

b=a()  #외부함수 호출: a 함수
b()  #내부함수 호출: b 함수

# 1-2.함수 클로저
data=list(range(1,101))  #range 1부터 100까지 하고 이 숫자를 리스트화 시킨 것.
def outer_func(data):
    dataset=data  #값(1~100)생성
    #inner
    def tot():
        tot_val=sum(dataset)  #sum=1~100까지의 합
        return tot_val
    def avg(tot_val):
        avg_val=tot_val/len(dataset)  #avg=sum값/100
        return avg_val
    return tot, avg  #inner 반환

# 외부함수 호출: data 생성
tot, avg=outer_func(data)

# 내부함수 호출
tot_val=tot()
print('tot=',tot_val)
avg_val=avg(tot_val)
print('avg=',avg_val)

# 2.중첩함수 역할
# 외부함수: 함수에서 사용할 자료를 만들고 내부함수를 포함
# 내부함수: 외부함수에서 만든 자료를 연산하고 조작하는 역할
from statistics import mean  # 평균
from math import sqrt  # 제곱근

data = [4, 5, 3.5, 2.5, 6.3, 5.5]


# 2-1.외부함수: 산포도 함수
def scattering_func(data):  # outer
    dataSet = data  # data 생성

    # 2-2.내부함수: 산술평균 반환
    def avg_func():
        avg_val = mean(dataSet)
        return avg_val

    # 2-3.내부함수: 분산 반환
    def var_func(avg):
        diff = [(data - avg) ** 2 for data in dataSet]
        # print(sum(diff))  #차의 합
        var_val = sum(diff) / (len(dataSet) - 1)
        return var_val

    # 2-4.내부함수: 표준편차 반환
    def std_func(var):
        std_val = sqrt(var)
        return std_val

    # 함수 클로저 반환
    return avg_func, var_func, std_func


# 외부함수 호출
avg, var, std = scattering_func(data)
# 내부함수 호출
print('평균:', avg())
print('분산:', var(avg()))
print('표준편차:', std(var(avg())))


# 3.획득자, 지정자, nonlocal
# def 외부함수 ():
#     변수명=값
#    def 내부함수 ():
#        nonlocal 변수명
# 3-1.중첩함수 정의
def main_func(num):
    num_val = num  # 자료생성

    def getter():  # 획득자 함수, return 있음
        return num_val  #반드시 return 명령문 있음

    def setter(value):  # 지정자 함수 있음
        nonlocal num_val  # nonlocal 명령어 (외부 함수에서 생성된 자료 수정할 경우 쓰이는 nonlocal)
        num_val = value  #반드시 매개변수 있음

    return getter, setter  # 함수 클로저 반환


# 3-2.외부함수 호출
getter, setter = main_func(100)  # num 생성
# 3-3.획득자 호출
print('num=', getter())  # 획득한 num 확인
# 3-4.지정자 획득
setter(200)  # num 값 수정
print('num=', getter())  # num 수정 확인


# 4.함수 장식자
# 4-1.래퍼 함수
def wrap(func):
    def decorated():
        print('반가워요!')  #시작 부분에 삽입
        func()  #인수로 넘어온 함수 (hello)
        print('잘가요~')  #종료 부분에 삽입
    return decorated  #클로저 함수 반환
# 4-2.함수 장식자 적용
@wrap  #함수 장식자는 @함수명 형태로 함수 앞에 '@'기호 삽입
def hello():
    print('hi~','홍길동')
# 4-3.함수 호출
hello()


# 5.재귀함수
# 재귀함수는 함수 내부에서 자신의 함수를 반복적으로 호출하는 함수
# 반복적으로 호출하는 함수라서 탈출exit조건 필수
# 재귀함수에서 재귀호출이 발생할 때 생성된 자료는 Stack이라는 메모리 영역에 저장됨

# 5-1.카운트
# 재귀함수 정의: 1~n 카운트
def Counter(n):
    if n==0:
        return 0  #종료 조건
    else:
        Counter(n-1)  #재귀 호출
        print(n,end='')
# 5-2.함수 호출1
print('n=0:',Counter(0))
# 5-3.함수 호출2
Counter(5)

# 재귀함수 정의: 1~n 누적합(1+2+3+4+5)
def Adder(n):
    if n==1:  #종료 조건
        return 1
    else:
        result=n+Adder(n-1)  #재귀호출

        print(n,end='')  #스택 영역
        return result

# 함수 호출
print('n=1:', Adder(1))  #n=1:1
print('\nn=5:',Adder(5))  #n=5:15 / \n은 한 줄 띄우기


