
# 1.모듈 추가 (방법1)
# 형식)import 패키지명.모듈명
import chapter06.myPackage.scattering

# 데이터 셋
data=[1,3,1.5,2,1,3.2]

# 산술평균 함수 호출
print('평균:',chapter06.myPackage.scattering.Avg(data))  #평균: 1.95

# 분산과 표준편차 함수 호출
var,sd=chapter06.myPackage.scattering.var_sd(data)
print('분산:',var)  #분산: 0.9350000000000002
print('표준편차:',sd)  #표준편차: 0.9669539802906859


# 2.모듈 추가 (방법2)
# 형식) from 패키지명.모듈명 import 함수명
from chapter06.myPackage.scattering import Avg, var_sd

print('평균:', Avg(data))  #평균: 1.95
var, sd=var_sd(data)
print('분산:',var)  #분산: 0.9350000000000002
print('표준편차:',sd)  ##표준편차: 0.9669539802906859