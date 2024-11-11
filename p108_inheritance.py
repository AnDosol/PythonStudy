# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 15:15:37 2024

@author: Administrator
"""

# 다중 상속
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
    def show(self):
        print(self.name,self.age)

        
class Student:
    def __init__(self,id):
        self.id=id
        
    def getId(self):
        return(self)
    
class CollageStudent(Person,Student):
    def __init__(self,name,age,idnum):
        #super().__init__(self,name,age)
        #super().__init__(self,id)  ==> 다중일 때는 안됨
        Person.__init__(self, name, age)
        Student.__init__(self, id)        
        
obj=CollageStudent('kim', 22, '20241024')
obj.show()
print(obj.getId())