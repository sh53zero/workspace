
# 다음 height 변수에 별(star)의 층수를 입력하면 각 층 마다 별의 개수가 한 개씩 증가하여 출력되고, 마지막 줄에 별의 개수가 출력되도록 빈 칸을 채우시오.

# <출력 결과 예시>
# height: 3 <- 키보드 입력
# *
# **
# ***
# start 개수: 6

def StarCount(height):
    if height==0:
        return 0
    else:
        StarCount(height-1)
        print(height, end='')

# 키보드 입력
height=int(input('height:'))
StarCount(3)
# start 개수 출력
print('star 개수: %d' %StarCount(height))

# 정답
def StarCount(height):
    h_cnt=s_cnt=0

    while h_cnt<height:  #h_cnt는 높이
        h_cnt+=1  #h_cnt=h_cnt+1
        print('*' * h_cnt)
        s_cnt+=h_cnt
    return s_cnt

print('star 개수:', StarCount(3))