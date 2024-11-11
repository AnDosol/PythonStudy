# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 15:08:37 2024

@author: Administrator
"""

# 3개의 정수를 동시에 입력 받아 if else 사용하여
# 가장 작은 값을 구한다
# 3개의 정수를 입력하시오:10, 20, 30
# 제일 작은 정수는 10입니다.

a, b, c=map(int,input("정수 3개를 입력하세요:").split(','))
        #eval(input("정수 3개를 입력하세요:") => , 입력해야지 정상적으로됨
"""
min=100

if min>=a:
        min=a
elif min>=b:
        min=b
elif min>=c:
        min=c
"""
if a>b:
    if c>b:
        print("제일 작은 정수는",b,"입니다")
    else:
        print("제일 작은 정수는",c,"입니다")
else:
    if c>a:
        print("제일 작은 정수는",a,"입니다")
    else:
        print("제일 작은 정수는",c,"입니다")    
        
#print("제일 작은 정수는 "+str(min)+"입니다.")