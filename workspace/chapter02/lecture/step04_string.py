# 1.문자열 유형

oneLine="this is one line string"
print(oneLine)

multiLine="""this is
multi line
string"""
print(multiLine)  #"""은 줄바꿈 인식해서 출력함

multiLine2="this is \nmulti line \nstring"  #\n은 줄바꿈 용
print(multiLine2)


# 2.색인(index)
# 2-1.문자열 색인
string="PYTHON"
print(string[0])  #P
print(string[5])  #N
print(string[-1])  #N
print(string[-6])  #P

# 2-2.문자열 연산
print("python"+"program") #결합연산자 / python program
#print("python-"+3.7+".exe") #error / cuz, str and int cannot be together
print("python-"+str(3.7)+".exe") #python-3.7.exe
print("-"*30) #반복연산자 / ------------------------------


# 3.슬라이싱(slicing)
# 3-1.왼쪽 기준
print(oneLine)  #this is one line string
print("문자열 길이:",len(oneLine))  #문자열 길이: 23 / 공백(띄어쓰기)도 문자에 포함시킴!!
print(oneLine[0:4])  #왼쪽부터 4의 앞까지 / this
print(oneLine[:4])  #왼쪽부터 4의 앞까지 / this
print(oneLine[:])  #전체원소 / this is one line string
print(oneLine[::2])  #2의 배수로 index / ti soeln tig

# 3-2.오른쪽 기준
print(oneLine[0:-1:2]) #처음부터 오른쪽 끝의 바로 앞까지 2의 배수로 index / ti soeln ti
print(oneLine[-6:-1])  #-6부터 오른쪽 끝의 바로 앞까지 / strin
print(oneLine[-6:])  #-6의부터 끝까지 / string

# 3-3.부분 문자열 생성
subString=oneLine[-11:]  #-11부터 끝까지
print(subString)  #line string
print(oneLine[-11:-6])  #line / -11부터 -6의 앞까지임!


# 4.문자열 구분 함수
# 4-1.특정 글자 수 반환
print('t 글자수:', oneLine.count('t'))  #t 글자수: 2

# 4-2.접두어 문자 비교 판단
print(oneLine.startswith('this'))  #True
print(oneLine.startswith('that'))  #False

# 4-3.문자열 교체
print(oneLine.replace('this', 'that'))  #that is one line string

# 4-4.문자열 분리 / 문단->문장
sent=multiLine.split('\n')  #문단을 문장 단위로 구분할 땐 \n
print('문장:', sent)  #문장: ['this is', 'multi line', 'string']

# 4-5.문자열 분리 / 문장->단어
words=oneLine.split(' ')  #문장을 단어 단위로 구분할 땐 ' '
print('단어:', words)  #단어: ['this', 'is', 'one', 'line', 'string']
#★언론 등에서 가장 이슈되는 단어 분석할 때 쓰는 함수

# 4-6.문자열 결합 / 단어->문장
sent2=','.join(words)  #'구분자;.join(string) / ,(콤마)로 단어들을 결합해라~
print(sent2)  #this,is,one,line,string






