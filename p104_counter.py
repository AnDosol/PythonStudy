# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 11:33:11 2024

@author: Administrator
"""

class Counter:
    def __init__(self):
        self.count=0
        
    def increment(self):
        self.count+=1
        
    #def __str__(self):
        #pass
    def __str__(self): #값을 나오게 해줌
        mag="카운터 값:"+str(self.count)
        return mag
    
a = Counter()
#print(a)
print(a)
print(a.count)
a.increment()
print(a.count)

a = Counter()
#print(a)
print(a)
print(a.count)
a.increment()
print(a.count)