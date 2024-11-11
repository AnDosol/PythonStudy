# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 11:27:34 2024

@author: Administrator
"""

class Counter:
    def __init__(self,initValue=0):
        self.count=initValue
        print(self.count)
        
a=Counter()
print(a)
print(a.count)

a=Counter()
print(a)
print(a.count)

a=Counter(100)
print(a)
print(a.count)

b=Counter(200)
print(b)
print(b.count)

b=Counter()
print(b)
print(b.count)

