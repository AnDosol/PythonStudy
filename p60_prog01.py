# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 11:12:57 2024

@author: Administrator
"""

# 입력하는 정수값을 리스트에 저장하고 이 값들의 합계를 구한
# for, appendm input, sum




n=int(input("입력할 값의 갯수:"))
result=[]

for i in range(n):
    value = int(input("값을 입력하세요:"))
    result.append(value)
s=sum(result)
print("값의 합계=", s)
