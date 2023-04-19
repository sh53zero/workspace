
def bank_account(bal):
    balance=bal

    def getBalance():
        return balance

    def deposit(money):
        nonlocal balance
        balance+=money


    def withdraw(money):
        nonlocal balance
        if money > balance:
            print('잔액이 부족합니다.')
        else:
            balance -= money
    return getBalance, deposit, withdraw


bal=int(input('최초 계좌의 잔액을 입력하세요:'))
getBalance, deposit, withdraw=bank_account(bal)
print('현재 계좌 잔액은'+str(getBalance())+'원 입니다.')

#왜 안 알려주세요..?
deposit()=int(input('입금액을 입력하세요:'))
print(str(deposit())+'원 입금후 잔액은'+str(bank_account())+'원 입니다.')