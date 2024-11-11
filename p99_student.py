# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 16:48:22 2024

@author: Administrator
"""

class Student:
    name1=None
    __name2=None #private
    
    def __init__(self,name1,name2):
        self.name1=name1
        self.__name2=name2
        
s=Student("Hong","Hong2")
print(s.name1)
#print(s.__name2)
print(s._Student__name2)

s.__name2="Hong3"
print(s.__name2)
print(s._Student__name2)