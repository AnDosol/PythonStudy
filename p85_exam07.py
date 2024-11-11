# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 10:21:09 2024

@author: Administrator
"""
"""
s1=input("첫 번째 문자열:") # Hello World!
s2=input("두 번째 문자열:") # Hi! Welcome

set1=set(s1)
print("set1:",set1)
set2=set(s2)
print("set2:",set2)

print("모두 포함된 글자:",set1 and set2)
"""

print(bool(13))
print(0b1101 & 0b1001)
print(13&9)
print(13 and 9)
print(0 and 9) # (x,y) if x is false, then x, else y

print(bin(0b1101 & 0b1001))
print(bin(9))

print(bin(0b0010 & 0b1101))
print(bin(0b1101 & 0b0010))

print(13 and 2)
print(0 and 12)
print(13 or 2)

n=10
print(n << 1) # 비트 연산자 왼쪽 1칸 이동 오른쪽 0으로 채움
print(n >> 1) # 왼쪽은 부호비트 
print(n << 2) 
print(n >> 2)
print(n << 3)
print(n >> 3)

n=-10
print(n << 1) 
print(n >> 1)  
print(n << 2) 
print(n >> 2)
print(n << 3)
print(n >> 3)
