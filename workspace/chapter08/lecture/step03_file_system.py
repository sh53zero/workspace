
try:
    with open('../data/ftest3.txt',mode='w',encoding='utf-8') as ftest:
        ftest.write('파이썬 파일 작성 연습')
        ftest.write('\n파이썬 파일 작성 연습2')
        # with 블록 벗어나면 자동 close

    with open('../data/ftest3.txt',mode='r',encoding='utf-8') as ftest:
        print(ftest.read())

except Exception as e:
    print('Error 발생:',e)

finally:
    pass