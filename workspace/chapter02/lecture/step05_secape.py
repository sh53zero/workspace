# 1.이스케이프 문자
# 1-1.escape 문자 적용
print('escape 문자 차단')  #escape 문자 차단
print('\n출력 이스케이프 문자')  #(줄바꿈)출력 이스케이프 문자

# 1-2.escape 문자 기능 차단
print('\\n출력 이스케이프 기능 차단1')  #\n출력 escape 기능 차단1
print(r'\n출력 이스케이프 기능 차단2')  #r은 escape 기능을 차단함 / \n출력 이스케이프 기능 차단2

# 1-3.경로 표현 :C:\Python\test
print('path=', 'C:\Python\test')  #\p이스케이프문자 없으나 \t는 이스케이프문자 있어서 escape처리됨 / path= C:\Python	est
print('path=', 'C:\\Python\\test')  #path= C:\Python\test / \\는 \ 하나로만 표기됨
print('path=', r'C:\Python\test')  #escape기능 차단시킨 r''이 있어서 / path= C:\Python\test