# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 11:41:25 2024

@author: Administrator
"""

class Cat:
    def __init__(self,name,age):
        self.__name=name
        self.__age=age
        
    def setName(self,name):
        self.__name=name
    
    def getName(self):
        return self.__name

    def setAge(self,age):
        self.__age=age     
        
    def getAge(self):
        return self.__age
    
missy=Cat('Missy', 3)
lucky=Cat('Lucky', 5)

print(missy.getName(),missy.getAge())
print(lucky.getName(),lucky.getAge())