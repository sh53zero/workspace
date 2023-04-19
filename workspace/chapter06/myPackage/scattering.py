
# 1-1.평균과 제곱근 모듈 import
from statistics import mean
from math import sqrt

# 1-2.산술평균 함수
def Avg(data):
    avg=mean(data)
    return avg

data=[2,4,5,6,1,8]
print('평균=', Avg(data))  #평균=4

# 1-3.분산/표준편차 함수
def var_sd(data):
    avg=Avg(data)
    diff=[(d-avg)**2 for d in data]
    var=sum(diff) / (len(data)-1)
    sd=sqrt(var)

    return var,sd

print('평균=', Avg(data))
var,sd=var_sd(data)
print('분산=', var)
print('표준편차=',sd)

# 프로그램 시작점
if __name__=='__main__':
    data=[1,3,5,7]
    print('평균:', Avg(data))  #평균: 4
    var, sd = var_sd(data)
    print('분산=', var)  #분산= 6.666666666666667
    print('표준편차=', sd)  #표준편차= 2.581988897471611

