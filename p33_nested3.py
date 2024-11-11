# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 14:55:41 2024

@author: Administrator
"""

adj=["small","medium", "large"] #list(중요), 배열
nums=["apple", "banana", "grape"]

for x in adj:
    print(x)
    
for y in nums:
    print(y)
    
    
for x in adj:
    for y in nums:
        print(x,y)