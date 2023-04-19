
# 1-1.현재 작업디렉터리
import os
print('\n현재경로:',os.getcwd())  #현재경로: E:\Pywork\workspace\chapter08\lecture

# 1-2.예외처리
try:
    # 1-3.파일 읽기
    ftest1=open('../data/ftest.txt',mode='r')  #<- ../으로 하는 이유, 위치 재정비 (..은 상위로 올라간다는 뜻)
    print(ftest1.read())  #파일 전체 읽기

    # 1-4.파일 쓰기
    ftest2=open('../data/ftest2.txt',mode='w')
    print(ftest2.write('my first text~~~'))  #파일 쓰기

    # 1-5.파일 쓰기+내용 추가
    ftest3=open('../data/ftest2.txt', mode='a')
    ftest3.write('\nmy second text~~~')  #파일 쓰기 추가

except Exception as e:
    print('Error 발생:',e)

finally:
    ftest1.close()  #파일 객체 닫기
    ftest2.close()
    ftest3.close()


# 2-1.파일 읽기 관련 함수
try:

    # 2-2.read(): 전체 텍스트 자료 읽기
    ftest=open('../data/ftest.txt', mode='r')
    full_text=ftest.read()
    print(full_text)
    print(type(full_text))  #<class 'string'>

    # 2-3.readlines(): 전체 텍스트 줄 단위 읽기
    ftest=open('../data/ftest.txt',mode='r')
    lines=ftest.readlines()  #list 반환
    print(lines)  #['programming is fun\n', 'very fun!\n', 'have a good time\n', 'mouse is input device\n', 'keyboard is input device\n', 'computer is input output system']
    print(type(lines))  #<class 'list'>
    print('문단수:',len(lines))

    # 2-4.list->문장 추출
    docs=[]  #문장 저장
    for line in lines:
        print(line.strip())  #text만 출력 / ['programming is fun', 'very fun!', 'have a good time', 'mouse is input device', 'keyboard is input device', 'computer is input output system']
        docs.append(line.strip())

    print(docs)  #문장 출력

    # 2-5.readline(): 한 줄 읽기
    ftest=open('../data/ftest.txt',mode='r')
    line=ftest.readline() #한 줄 읽기
    print(line)  #programming is fun
    print(type(line))



except Exception as e:
    print('Error 발생:',e)

finally:
    # 파일 객체 닫기
    ftest.close()