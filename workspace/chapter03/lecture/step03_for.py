import random

# 1.for 반복문 예
# 1-1.문자열 열거형객체 이용
string='홍길동'
print(len(string))  #문자 길이:3
for s in string:  #1문자->변수 넘김: 3회
    print(s)

# 1-2.list 열거형객체 이용
lstset=[1,2,3,4,5]  #5개 원소를 갖는 열거형객체
for e in lstset:  #e는 집합의 원소
    print('원소:',e)

# 2.range
# 2-1.range 객체 생성
num1=range(10)  #range(stop) / range(start, stop, step)
print('num1:',num1)  #num1: range(0,10)
num2=range(1,10)  #range(start,stop)
print('num2:',num2)  #num2: range(1,10)
num3=range(1,10,2)  #range(start,stop,step)
print('num3:',num3)  #range(1,10,2)

# 2-2.range 객체 활용
for n in num1:
    print(n, end=' ')  #0 1 2 3 4 5 6 7 8 9 (10이전까지만 출력)
print()
for n in num2:
    print(n, end=' ')  #1 2 3 4 5 6 7 8 9
print()
for n in num3:
    print(n, end=' ')  #1 3 5 7 9 (step=증가라서 2씩 증가)

# 3.list
# 3-1.list에 자료 저장하기
lst=[]  #빈 list 만들기
for i in range(10):  #0~9
    r=random.randint(1,10)  #난수 발생 <-무작위로 랜덤 출력
    lst.append(r)  #난수 저장
print('lst=',lst)  #난수 출력

# 3-2.list에 자료 참조하기
for i in range(10):  #0~9
    print(lst[i]*0.25)  #난수*0.25 <- 위에 무작위로 출력한 난수들*0.25 값들


# 4.중첩반복문
# 4-1.구구단 예시
# 구구단 출력: range() 함수 이용
# 바깥쪽 반복문
for i in range(2,10):  #2단
    print('~~~{}단 ~~~'.format(i))

    #안쪽 반복문  #1~9 곱하기
    for j in range(1,10):
        print('%d*%d=%d'%(i,j,i*j))


# 5.문장과 단어 추출 예
string="""나는 홍길동 입니다.
주소는 서울시 입니다.
나이는 35세 입니다."""

sents=[]  #문장 저장
words=[]  #단어 저장

# 5-1. 문단->문장
for sen in string.split(sep="\n"):  #sen을 문장으로 나눠라
    sents.append(sen)  #나뉘어진 sen을 저장해라
    for word in sen.split():  #나뉘어진 sen을 단어로 나눠라
        words.append(word)  #word를 저장해라

print('문장:', sents)
print('문장수:', len(sents))
print('단어:', words)
print('단어수:', len(words))


