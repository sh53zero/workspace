
# 1.클래스 캡슐화
class Account:
    # 1-1.은닉 멤버변수
    __balance=0  #잔액
    __accName=None  #예금주
    __accNo=None  #계좌번호

    # 1-2.생성자"멤버변수 초기화
    def __init__(self,bal,name,no):
        self.__balance = bal  #잔액 초기화
        self.__accName = name  #예금주
        self.__accNo = no #계좌번호

    # 1-3.계좌정보 확인 : Getter
    def getBalance(self):
        return self.__balance, self.__accName, self.__accNo

    # 1-4.입금하기: Setter
    def deposit(self,money):
        if money<0:
            print('금액확인')
            return  #종료
        self.__balance+=money

    # 1-5.출금하기 :Setter
    def withdraw(self,money):
        if self.balance<money:
            print('잔액 부족')
            return  #종료
        self.__balance -= money

# 1-6.object 생성
acc=Account(1000,'홍길동','125-152-4125-41')  #생성자

# 1-7.Getter 호출
#acc.__balance #오류 뜸
bal=acc.getBalance()  #__balance가 은닉되었기때문에 getter를 사용해서 얻어야 함
print('계좌정보:',bal)
acc.deposit(10000)  #10,000원 입금
bal=acc.getBalance()
print('계좌정보:', bal)  #입금 확인

