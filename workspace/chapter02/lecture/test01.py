
# 1.
#<조건1> 수량변수: su=5
#<조건2> 단가변수: dan=800
#<조건3> su, dan 변수 주소 확인
#<조건4> 금액 계산=수량x단가
#<조건5> 기타 세부내용 <출력 화면 예시> 참고
#출력화면 예시 su 주소: ~~
#           dan 주소: ~~
#           금액= 4000

su=5
dan=800
price= su*dan
print('수량변수: su=', su)
print('단가변수: dan=', dan)
print('su 주소:', id(su))
print('dan 주소', id(dan))
print('금액=', price)


# 2.
#3개의 단어를 키보드로 입력 받아서 각 단어의 첫글자를 추출하여 단어의 약자를 출력하시오.
#<조건1> 각 단어 변수(word1, word2, word3) 저장
#<조건2> 입력과 출력 구분선: 문자열 연산
#<조건3> 각 변수의 첫 단어만 추출하여 변수(abbr) 저장
#출력화면 예시
#첫번째 단어: Korea
#두번째 단어: Baseball
#세번째 단어: Orag
#===============
#약자: KBO

word1=input("첫번째 단어:")
word2=input("두번째 단어:")
word3=input("세번째 단어:")

abbr=word1[0]+word2[0]+word3[0]
print('='*15)
print('약자:'+abbr)


