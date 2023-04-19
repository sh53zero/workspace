
# 1.반복문
# 1-1.카운터와 누적변수
cnt = tot = 0 #변수 초기화
while cnt<5: #카운터 변수
    cnt +=1 #카운터 변수(cnt=cnt"1)
    tot +=cnt #누적변수: tot=tot+cnt
    print(cnt,tot)

#실습 1~100 사이 3의 배수 합과 원소 추출하기
cnt=tot=0
dataset=[] #빈 list
while cnt <100: #100회 반복
    cnt +=1 #카운터
    if cnt %3==0:
        tot +=cnt #누적변수
        dataset.append(cnt) #cnt 추가

print('1~100 사이 3의 배수 합 = %d' %tot)
print('dataset=', dataset)


# 1-2.무한루프 (loop)
numData=[] #빈 list

while True:  #while True를 쓸 경우 무한루프를 돌 수 있기 때문에 꼭 exit 조건식이 필요함
    num = int(input('숫자 입력:'))

    if num %10==0: #exit 조건식
        print("프로그램 종료")
        break
    else:
        print(num)
        numData.append(num) #list 추가


# 2.random 모듈
# 2-1.random module 추가
import random
help(random) # 모듈 도움말

# 2-2.random 모듈의 함수 도움말
help(random.random)

# 2-3.0~1 사이 난수 실수
import random
r=random.random()
print('r=',r)  #r=0.3940

#[실습] 난수 0.01 미만이면 종료 후 난수 개수 출력
cnt=0
while True:
    r=random.random()
    print(r)
    if r<0.01:
        break  #loop exit
    else:
        cnt+=1

print('난수 개수=', cnt)


# 2-4.random 모듈 관련 함수 도움말
help(random.randint)
help(random.choices)  #모집단에서 k크기 목록 반환

# 2-5.이름 list에 전체 이름, 특정 이름 출력
names= ['홍길동', '이순신', '유관순']
print(names)  #전체 이름
print(names[2])  #특정 이름 출력

# 2-6.list에서 자료 유무 확인하기
if '유관순' in names:
    print('유관순 있음')
else:
    print('유관순 없음')

# 2-7.난수 정수로 이름 선택하기
idx=random.randint(0,2)
print(names[idx])

# 2-8.break, continue 예
i=0
while i<10:
    i+=1  #카운터
    if i==3:
        continue  #다음문장 skip
    if i==6:
        break  #탈출조건 exit
    print(i,end='')
