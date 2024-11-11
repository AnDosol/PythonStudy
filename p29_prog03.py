# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 10:14:14 2024

@author: Administrator
"""

import random

x=random.randint(1,10) # 5
y=random.randint(1,10) # 3
op=random.randint(0,3) # 0,1,2,3(+,-,*,/)

print(op)

if op == 0: # 5+3 "의 덧셈 결과는?"
    answer=int(input(str(x)+"+"+str(y)+"의 덧셈 결과는?"))
    if x+y == answer:
        print("맞습니다.")
    else:
        print("틀렸습니다")
        
elif op == 1: # 5+3 "의 뺄셈 결과는?"
    answer=int(input(str(x)+"-"+str(y)+"의 뺄셈 결과는?"))
    if x-y == answer:
        print("맞습니다.")
    else:
        print("틀렸습니다")        

elif op == 2: # 5+3 "의 덧셈 결과는?"
    answer=int(input(str(x)+"*"+str(y)+"의 곱셈 결과는?"))
    if x*y == answer:
        print("맞습니다.")
    else:
        print("틀렸습니다")
        
elif op == 3: # 5+3 "의 나눗셈 결과는?"
    answer=int(input(str(x)+"/"+str(y)+"의 나눗셈 결과(몫)는?"))
    if int(x/y) == answer:
        print("맞습니다.")
    else:
        print("틀렸습니다")        