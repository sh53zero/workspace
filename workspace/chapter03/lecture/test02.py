
#multiline을 이용해서 단어 갯수 출력하시오

multiline="""안녕하세요. 파이썬 세계로 오신걸
환영합니다.
파이썬은 비단뱀처럼 매력적인 언어입니다."""

sents=[]
words=[]

for sen in multiline.split(sep="\n"):
    sents.append(sen)
    for word in sen.split():
        words.append(word)
        print(word)

print(sents)
print('문장수:',len(sents))
print(words)
print('단어수:',len(words))


#정답
multiline="""안녕하세요. 파이썬 세계로 오신걸
환영합니다.
파이썬은 비단뱀처럼 매력적인 언어입니다."""

cnt=0
doc=[]
word=[]
for line in multiline.split("\n"):
    doc.append(line)
    for w in line.split():
        word.append(w)
        print(w)  #줄바꿈된 형태의 출력은 <<print를 여기에 삽입.
        cnt+=1  #clear 시키는 함수가 있어야 함. 코딩의 법칙

print('단어수:', cnt)
print(doc)
print(word)
