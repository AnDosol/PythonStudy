# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 14:14:27 2024

@author: Administrator
"""

heroes=["C","C++","Arduino","Python","Raspberry"]
n=heroes.index("Arduino")
print("n=",n)


if "Arduino" in heroes:
    print(heroes.index("Arduino"))
    
# 탐색을 시작하는 위치 지정
n=heroes.index("Arduino",1)
print("n=",n)

heroes.remove("Arduino")
print(heroes)

# 만일 C++이 있다면 제거하세요
if "C++" in heroes:
    heroes.remove("C++")
print(heroes)

h=heroes.pop(2)
print(heroes)
print(h)

values=[1,2,3,4,5,6,7,10,9,8]
ma=max(values)
mi=min(values)
print(ma,mi)


values.sort() # 오름차순
print(values)

values.sort(reverse=True) # 내림차순
print(values)