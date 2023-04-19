
class DatePro:
    # 1-1.멤버 변수
    content="날짜 처리 클래스"

    # 1-2.생성자
    def __init__(self,year,month,day):
        self.year=year
        self.month=month
        self.day=day


    # 1-3.객체 메소드 (instance method)
    def display(self):
        print('%d-%d-%d' %(self.year, self.month, self.day))

    # 1-4.클래스 메소드  -> class 이름이 DatePro
    @classmethod  #함수 작성자
    def date_string(cls,dateStr):  #'19951025'
        year=dateStr[:4]
        month=dateStr[4:6]
        day=dateStr[6:]

        print(f'{year}년 {month}월 {day}일')

# 1-5.객체 멤버
date=DatePro(1995,10,25)  #생성자
print(date.content)  #날짜 처리 클래스
print(date.year)
date.display()

# 1-6.클래스 멤버
print(DatePro.content)
#print(DatePro.year)
DatePro.date_string('19951025')