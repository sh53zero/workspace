
import pickle

# 1-1.pickle file load
file=open('/chapter090/data/data.pickle', mode='rb')
news_data2=pickle.load(file)

# 1-2.텍스트 전처리
import re

def clean_text(text_string):
    # 문장부호 제거
    text_string_re=re.sub('[,.?!:;\'\"]','',text_string)
    # 특수문자, 숫자 제거
    text_string_re=re.sub('[!@#$%^&*()]|[0-9]','',text_string_re)  #|는 or의 뜻
    # 영문 소문자->영문 제거
    text_string_re=text_string_re.lower()
    text_string_re=re.sub('[a-z]','',text_string_re)
    # 공백 제거
    text_string_re=' '.join(text_string_re.split())

    return text_string_re

# 텍스트 전처리 함수 호출
clean_texts=[clean_text(row) for row in news_data2]
print('>>텍스트 전처리 결과<<')
print(clean_texts)

# 1-3.word count
word_count={}

for text in clean_texts: #텍스트->문장
    for word in text.split():  #문장->단어
        word_count[word]=word_count.get(word,0)+1
print('>>워드 카운트<<')
print(word_count)

# 1-4.단어 전처리
# 불용 단어 제거
del word_count['결국']

# 3회 이상 출현 단어 & 2~4자 단어 선정
new_word_count={}
for word, cnt in word_count.items():
    if cnt >=2 and len(word) >=1 and len(word)<=2:
        print(word,'->',word_count[word])
        new_word_count[word]=new_word_count.get(word,cnt)

print('>>단어 전처리<<')
print(new_word_count)

# 1-5.top word Counter
from collections import Counter  #모듈 추가

counter=Counter(new_word_count)
top5_word=counter.most_common(5)  #top5
print('>>top5 단어<<')  #[('尹', 2), ('겨냥', 2), ('野', 2), ('개최', 2), ('中', 2)]
print(top5_word)


# 2-1.단어와 출현 빈도수 만들기
words=[]  #단어
counts=[]  #출현빈도수

for word, count in top5_word:
    words.append(word)
    counts.append(count)

print(words)  #['尹', '겨냥', '野', '개최', '中']
print(counts)  #[2, 2, 2, 2, 2]

# 2-2.pyplot 모듈 import
import matplotlib.pyplot as plt

# 2-3.차트에서 한글 지원
from matplotlib import font_manager, rc
font_name=font_manager.FontProperties(fname='c:/Windows/Fonts/malgun.ttf').get_name()
rc('font', family=font_name)

# 2-4.선 그래프
print('선 그래프')
plt.plot(words,counts)  #그리기
plt.show()

# 2-5.막대 그래프
print('막대 그래프')
plt.plot(words,counts)  #그리기
plt.show()