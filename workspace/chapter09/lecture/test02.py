
import pandas as pd
import matplotlib.pyplot as plt  #pyplot은 그래프 그리는 것, as pd는 앞의 것을 pd로 칭하는 것

# 조건1
iris=pd.read_csv('/chapter090/data/iris.csv')
print(iris.info())  #칼럼 등의 정보를 알고 싶으니 info 함수 사용

# 조건2
plt.scatter(iris['Sepal.Length'],iris['Petal.Length'])  #산점도

# 조건3: Species 칼럼으로 색상 적용
# 꽃의 종별 범주 확인
print(iris['Species'].unique())  #['setosa' 'versicolor' 'virginica'] / unique는 유일하단 뜻, 복수말고 하나로만 출력

#'setosa'=1, 'versicolor'=2, 'virginica'=3
species=[]
for s in iris['Species']:
    if s== 'setosa':
        species.append(1)
    elif s== 'versicolor':
        species.append(2)
    else:
        species.append(3)

# 수치화된 변수로 color 적용
plt.scatter(iris['Sepal.Length'], iris['Petal.Length'], c=species)
plt.xlabel('Sepal.Length')
plt.ylabel('Petal.Length')
plt.title('Sepal.Length vs Petal.Length scatter plotting')

plt.show()
