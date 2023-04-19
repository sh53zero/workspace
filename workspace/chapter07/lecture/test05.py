
from re import findall, sub
texts=['AFAB54747,asabeg?','abTTa $$;a12:2424', 'uysfsfA,A124&***$?']

def clean_text(text):
    text_re=text.lower()
    text_re2=sub('[0-9]','',text_re)
    text_re3=sub('[,.?!@#$%^&*();:]','',text_re2)
    text_re4=' '.join(text_re3.split())
    return text_re4

result=[clean_text(text) for text in texts]
print(result)
