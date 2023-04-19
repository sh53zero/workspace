
#
print('사각형의 넓이와 둘레를 계산합니다.')
w=int(input('사각형의 가로 입력:'))
h=int(input('사각형의 세로 입력:'))
class Rectangle:
    x=y=0

    def __init__(self,width,height):
        self.x=width
        self.y=height

    def area_calc(self):
        a=self.x*self.y
        return a

    def circum_calc(self):
        c=(self.x+self.y)*2
        return c

r=Rectangle(w,h)

print('='*40)
print('사각형의 넓이:',r.area_calc())
print('사각형의 둘레:',r.circum_calc())
print('='*40)