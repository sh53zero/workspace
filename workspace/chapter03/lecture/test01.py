
#항공사에서는 짐을 부칠 떄, 10kg이상부터 수수료를 내야한다. 수수료는 10의 배수 단위로 10,000원씩 증가한다.
#만약 10kg 미만이면 수수료는 없다. 사용자의 짐의 무게를 키보드로 입력받고, 사용자가 지불하여야 할 금액을 계산하는 프로그램을 작성하시오.

#<출력 결과 예시>
#짐의 무게는 얼마입니까? 8
#수수료는 없습니다.
#짐의 무게는 얼마입니까? 15
#수수료는 10,000원입니다.
#짐의 무게는 얼마입니까? 21
#수수료는 20,000원입니다.

#keypoint 는 10의 배수, 10으로 나눠서 몫으로 계산
#밑에건 오답~~
kg=int(input('짐의 무게는 얼마입니까?'))
price=10,000

if kg <10 :
    price='없습니다.'
elif kg >=10*n and kg<20
    price=
print('수수료는' + price )

elif kg >=10 and kg<20:
    price='i'
else :
    price='저조'
print('수수료는' +  , (kg, price))

#밑에건 정답~~
while True:  #무한루프 돌아야 함
    weight = int(input('짐의 무게는 얼마입니까?'))
    if weight == 0:  #그러나 0kg면 종료
        break;  #그래서 break 줌
    if weight >=10:  #if문으로 10 이상일 경우로 계산
        price=(weight//10)*10000  #weight를 10으로 나눈 후 몫과 수수료의 10000원을 곱함
        print('수수료는'+format(price,'3,d')+'입니다.')  #format함수 이용해서 3,d로 단위 표기함
    else:
        print('수수료는 없습니다.')  #10 이하는 else문으로 작성