# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 13:46:45 2024

@author: Administrator
"""

question=['name', 'quest', 'color']
answer=['Kim','Python','Blue']

# 두 개의 리스트를 서로 묶어준다
for q,a in zip(question,answer):
    #print("What is your "+q+" It is "+a)
    print(f"What is your {q} It is {a}")
    
    
heroes=[]
print(heroes)
heroes.append("C언어") # 추가 
heroes.append("Python")
heroes.append("C++")

print(heroes)

# 지정된 위치에 삽입