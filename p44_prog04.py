# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 10:10:42 2024

@author: Administrator
"""

"""
패스워드를 검증하는 함수 checkPass(p)를 작성하고
패스워드에는 적어도 8글자 이상이어야 한다.
또 적어도 1글자의 대문자와 소문자가 들어가야 한다.
또 적어도 1개의 숫자가 들어가야 한다.

isupper():대문자
islower():소문자
isdigit():숫자로만 구성된 문자열을 감지하는 함수
"""
"""
a=True
print("True:",a)

b=1
c=0

if b and b:
    print("True")
    
else:
    print("false")
    
if b and c:
    print("True")
    
else:
    print("false")
"""

def checkPass(p): # abcKKJ1234
    digit,lower,upper=0,0,0
    
    for i in p:    
        if i.isupper():
            upper=1
        elif i.islower():
            lower=1
        elif i.isdigit():
            digit=1
    if len(p) >= 8 and (upper==1 and lower==1 and digit==1):
        print("사용할 수 있습니다.")
        
    else:
        print("사용할 수 없습니다.")
        
checkPass(input("패스워드를 입력하세요:"))



































