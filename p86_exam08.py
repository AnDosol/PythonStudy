# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 11:45:13 2024

@author: Administrator
"""

set1=set([10,20,30,40,50,60])
print("set1:",set1)

set2=set([30,40,50,60,70,80])
print("set2:",set2)

print("set1 & set2:",set1 & set2)
print("어느 한쪽에만 있는 요소들 set1:",(set1)-(set1 & set2))
print("어느 한쪽에만 있는 요소들 set2:",(set2)-(set1 & set2))










