
# 1. 변수, 메모리 주소, 자료형
var1 = "Hello python"
print(var1)
print(id(var1))
print(type(var1))

var1 = 100
print(var1)
print(id(var1))
print(type(var1))

var2 = 150.25
print(var2)
print(id(var2))
print(type(var2))

var3 = True
print(var3)
print(id(var3))
print(type(var3))


# 2. 예약어 확인
import keyword # 모듈 임포트
python_keyword = keyword.kwlist
print(python_keyword)

print(type(python_keyword)) # <class 'list'>
print(len(python_keyword)) #35

# 3. 자료형 변환
# 3-1. 실수 -> 정수
a = int(10.5)
b = int(20.42)
add = a+b
print('add =', add)
print('a+b =', add)

# 3-2. 정수 -> 실수
a = float(10)
b = float(20)
add2 = a+b
print('add2 =',add2)
print('a+b =',add2)

# 3-3. 논리형 -> 정수
print(int(True)) #1
print(int(False)) #0

# 3-4. 문자형 -> 정수
st = '10'
print(int(st)**2) #제곱 연산

