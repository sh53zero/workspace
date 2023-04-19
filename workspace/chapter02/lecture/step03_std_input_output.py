
# 1.format 함수

# format() 함수 인수: format(value, "foramt")
print("원주율=", format(3.141592, "8.3f")) #      3.142
print("금액=", format(10000, "10d")) #     10000
print("금액=", format(125000, "3,d")) #125,000

# 양식문자 인수: print("%양식문자" "%값")
name= "홍길동"
age= 35
price= 123.456
print("이름:%s, 나이: %d, data=%.2f" %(name, age, price)) #이름: 홍길동, 나이:35, data=123.46

# 외부 상수 인수
print("이름:{}, 나이:{}, data={}" .format(name,age,price)) #이름:홍길동, 나이:35, data=123.456
print("이름:{1}, 나이:{0}, data={2}".format(age,name,price)) #이름:홍길동, 나이:35, data=123.456

# format 축약형 (SQL문 작성)
uid=input("id input:")
query=f"select*from member where uid= {uid}"
print(query) #member 테이블에서 uid가 hong인 레코드 검색  / #id input: >?hong
                                                # select * from member where uid = hong

