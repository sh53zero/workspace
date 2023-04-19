
# 다형성
# 여러 가지 형태를 가질 수 있는 능력

# 1-1.부모 클래스
class Flight:

    # 부모 원형 함수
    def fly(self):
        print('날다, fly 원형 메서드')

# 1-2.자식 클래스: 비행기
class Airplane(Flight):

    # 함수 재정의
    def fly(self):
        print('비행기가 날다.')

# 1-3.자식 클래스: 새
class Bird(Flight):

    # 함수 재정의
    def fly(self):
        print('새가 날다.')

# 1-4.자식 클래스: 종이비행기
class PaperAirplane(Flight):

    # 함수 재정의
    def fly(self):
        print('종이 비행기가 날다.')

# 1-5.부모 객체=자식 객체(자식1, 자식2)
flight=Flight()  #부모 클래스 객체
air=Airplane()  #자식1 클래스 객체
bird=Bird()  #자식2 클래스 객체
paper=PaperAirplane()  #자식3 클래스 객체


# 1-5.다형성
flight.fly()  #날다, fly 원형 메서드

flight=air
flight.fly()  #비행기가 날다.

flight=bird
flight.fly()  #새가 날다.

flight=paper
flight.fly()  #종이비행기가 날다.