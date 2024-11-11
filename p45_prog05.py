# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 11:27:55 2024

@author: Administrator
"""

# 10진수를 2진수로 변환(문자열) while,if,%,//

def deci2bin(n):
    binary=""
        
    while n!=0:
        value=n % 2
        if value == 0:
            binary="0"+binary
        else:
            binary="1"+binary
            
        n=n//2
        
    return binary

x=int(input("10진수:"))
print(deci2bin(x))