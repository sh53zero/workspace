
#오답
import  random
# 변수 정의하기
guesses=0  #시도 횟수 기록하기
numMin=1  #범위 시작 숫자
numMax=3  #범위 끝 숫자
userInput=""  #사용자 입력 저장하기

# 무작위 숫자 생성하기
randNum=random.randint(numMin,numMax)

while True:  #<<<< 이래서 계속 반복됨, 아래로 수정 필요
    randNum = random.randint(numMin, numMax)
    userInput = int(input('숫자 입력:'))
    # guesses=guesses+1이 없어서 시도횟수 0번 나옴
    if userInput > randNum:
        print('큽니다. 다시 입력해 주세요')
    elif userInput < randNum:
        print('작습니다. 다시 입력해 주세요.')
    else :
        print('정답입니다! 시도횟수:' + format(guesses) + '번')
print('정답입니다! 다음에 또 만나용')

# 정답
import random

# 변수 정의하기
guesses=0  #시도 횟수 기록하기
numMin=1  #범위 시작 숫자
numMax=100  #범위 끝 숫자
userInput=""  #사용자 입력 저장하기

# 무작위 숫자 생성하기
randNum=random.randint(numMin,numMax)

# 게임 설명문
print(numMin,'와(과)',numMax,'사이의 숫자 하나를 정했습니다.')
print('이 숫자는 무엇일까요?')

# 사용자가 맞힐 때까지 반복하기
while randNum != userInput:  #!!!!!! while True가 아니고 맞힐때까지 반복 !!!!!!
    # 사용자 답 입력받기
    userInput=int(input("예상 숫자:"))
    #시도 횟수 1회 늘리기
    guesses=guesses+1  #!!!!!! 시도 횟수 늘리기는 여기 있었다 !!!!!!!
    if userInput<randNum:
        print('작습니다. 다시 입력하세요.')
    elif userInput>randNum:
        print('큽니다. 다시 입력하세요.')
    else:
        print('정답입니다! 시도 횟수:',guesses, '번')

# 끝날 때 출력할 메세지
print('즐거우셨나요? 또 만나요!')

