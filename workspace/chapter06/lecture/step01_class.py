
# 1.클래스
# 1-1.함수 정의
def calc_func(a,b):  #외부함수
    # 변수 선언: 자료저장
    x=a
    y=b  #x와 y는 전역변수

    def plus():  #내부함수
        p=x+y
        return p #nonlocal을 쓰지 않은 이유, nonlocal은 x와 y에 값을 저장하기 위함.

    def minus():  #내부함수
        m=x-y
        return m
    return plus, minus

# 1-2.함수 호출
p,m=calc_func(10,20)
print('plus=',p())
print('minus=',m())

# 1-3.클래스 정의
class calc_class:
    # 클래스 변수: 자료저장
    x=y=0

    # 생성자: 객체 생성+멤버변수 초기화
    def __init__(self,a,b):
        self.x=a
        self.y=b

    def plus(self):
        p=self.x+self.y  #변수연산
        return p

    def minus(self):
        m=self.x-self.y  #변수연산
        return m

obj=calc_class(10,20)

print('plus=',obj.plus())
print('minus=',obj.minus())


class Car:
    # 2-1.멤버 변수
    cc=0  #엔진cc
    door=0  #문짝 갯수
    carType= None  #null

    # 2-2.생성자
    def __init__(self,cc,door,carType):
        # 멤버 변수 초기화
        self.cc=cc
        self.door=door
        self.carType=carType  #승용차, SUV

    # 2-3.메서드
    def display(self):
        print("자동차는 %d cc이고, 문짝은 %d개, 타입은 %s" %(self.cc,self.door,self.carType))

# 2-4.객체 생성
car1=Car(2000,4,'승용차')
car2=Car(3000,5,'SUV')

# 2-5.멤버 호출: object.member()
car1.display()  #car1 멤버 호출
car2.display()  #car2 멤버 호출