
email="""hong@12.com
you2@naver.com
12kang@hanmail.net
kimjs@gmail.com"""

from re import findall, match
for e in email.split(sep='\n'):

    result=(findall('^[a-z]{3,}@[a-z]{2,}.[a-z]{,2}',e))

    if result:
        str_result=result[0]
        print('findall:',str_result)

    result2=match('[a-z]{3,}@[a-z]{2,}.[a-z]{,2}',e)

    if result2:
        print('match:',e)






