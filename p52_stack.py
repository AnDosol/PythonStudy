# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 16:48:20 2024

@author: Administrator
"""

stack=[]
"""
for i in range(3): # 3번 반복
    f = input("과일을 입력하세요:")
    stack.insert(i, f)
    
print(stack)
"""
"""
for i in range(3): # 3번 반복
    f = input("과일을 입력하세요:")
    stack.append(f)
    
print(stack)
"""

for i in range(len(stack)): # 3번 반복
    
    print(stack.pop())
print(stack)