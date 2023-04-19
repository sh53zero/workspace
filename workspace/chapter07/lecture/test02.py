
from re import findall

emp=['2014홍길동220','2002이순신300','2010유관순260']

def name_pro(emp):
    names=[]

    for e in emp:
        name=findall('[가-힣]{3}',e)
        names.append(name[0]).

    return names

names=name_pro(emp)
print('names=',names)