# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 14:45:08 2024

@author: Administrator
"""
"""
class Student:
    def __init__(self,name=None,age=0):
        self.name=name
        self.age=age
        
        
obj=Student()
print(obj.name)
print(obj.age)
"""

class Student:
    def __init__(self,name=None,age=0):
        self.name=name
        #self.age=age
        self.__age=age
        print(self.__age)
        
    #print(self.__age)
        
obj=Student()
print(obj.name)
print(obj.__age)