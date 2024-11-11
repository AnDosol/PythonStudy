# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 13:51:56 2024

@author: Administrator
"""

def func1(x):
    x=42
    print("x=",x,"id=",id(x))
    
y=10
func1(y) 
print("y=",y,"id=",id(y))

def func2(list):
    list[0]=99
    print(id(list))
    print(list)
    
print()

values=[0,1,1,2,3,5,6] # 리스트 중복값 허용
print(id(values))
print(values)

func2(values)
print(values)

salaries=[200,250,300,280,500]

def modify(values, factor):
    for i in range(len(values)):
        values[i]=values[i]*factor

print("인상전", salaries)
modify(salaries,1.3)
print("인상후", salaries)





















