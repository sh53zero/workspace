
# 1.알고리즘
# 어떤 문제를 해결하기 위한 일련의 절차
# 프로그래밍의 논리적인 절차를 의미하는 로직의 기초
# 자료 입력->논리적인 순서에 의해 자료 처리->처리결과 출력: 프로그램

# 알고리즘의 조건
# 입력:외부에서 제공되는 자료
# 출력:적어도 한 가지 이상의 결과
# 명백성: 간단명료한 명령들
# 유한성: 반드시 종료 조건 필요
# 효과성: 명백하고 실행 가능한 명령들


# 2.최댓값/최솟값(max/min)
# 2-1.입력 자료 생성
import random
dataset=[]
for i in range(10):  #10개의 자료를 랜덤으로 출력
    r=random.randint(1,100)
    dataset.append(r)
print(dataset)

# 2-2.변수 초기화
vmax=vmin=dataset[0]

# 2-3.최댓값/최솟값 구하기
for i in dataset:
    if vmax < i:
        vmax=i
    if vmin > i:
        vmin=i

# 2-4.결과 출력
print('max=',vmax,'min=',vmin)

# 3.정렬
# 전체 자료의 원소를 일정한 순서로 나열하는 알고리즘.
# 오름차순 (ascending sort) 작은 수->큰 수
# 내림차순 (descending sort) 큰 수->작은 수
# 선택정렬 (selection sort)
# 버블정렬 (bubble sort)

# 3-1.오름차순 정렬
dataset=[3,5,1,2,4]
n=len(dataset)
for i in range(0,n-1):  #1~n-1
    for j in range(i+1,n):  #i+1~n
        if dataset[i]>dataset[j]:
            tmp=dataset[i]
            dataset[i]=dataset[j]
            dataset[j]=tmp
    print(dataset)  #각 회전 정렬내용 / [15324->12534->12354->12345]

print(dataset)  #[1,2,3,4,5]

# 3-2.내림차순 정렬
dataset=[3,5,1,2,4]
n=len(dataset)
for i in range(0,n-1):  #1~n-1
    for j in range(i+1,n):  #i+1~n
        if dataset[i]<dataset[j]:
            tmp=dataset[i]
            dataset[i]=dataset[j]
            dataset[j]=tmp
    print(dataset)  #각 회전 정렬내용 / [53124->54123->54312->54321]

print(dataset)


# 4.검색
# 4-1.이진검색
dataset=[5,10,18,22,35,55,75,103]  #이진검색은 정렬이 중요함! 이건 정렬되어있지만 안그렇다면 정렬함수 써야 함
value=int(input('검색할 값 입력:'))

low=0  #start 위치
high=len(dataset)-1  #end 위치
loc=0
state=False  #상태 변수 / 현 상태의 변수를 False로 만들어서 True 찾기로 하면 됨.

while (low<=high):
    mid=(low+high)//2  #2로 나눠서 몫을 취하기

    if dataset[mid]>value:  #중앙값이 큰 경우
        high=mid-1  # 나머지 값 버리고 대상 반으로 줄이는 이진검색
    elif dataset[mid]<value:  #중앙값이 작은 경우
        low=mid+1
    else:  #찾은 경우
        loc=mid
        state=True
        break  #while문 exit

#break로 빠져나온 후 상태 출력
if state:
    print('찾은 위치: %d 번째' %(loc+1))
else:
    print('찾는 값은 없습니다.')

