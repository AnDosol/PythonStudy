# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 17:02:36 2024

@author: Administrator
"""

class Employees:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
        
    def getSalary(self):
        return self.salary
    
class Manager(Employees):
    def __init__(self,name,salary,bonus):
        super().__init__(name, salary)
        self.bonus=bonus
        
    def getSalary(self):
        salary=super().getSalary()
        return salary+self.bonus
    
    def __str__(self):
        return "이름:"+self.name+";월급:"+str(self.salary)+";보너스:"+str(self.bonus)
    
kim=Manager("김철수",2000000,1000000)
print(kim)

print(kim.name+"총급여:"+str(kim.getSalary()))
print(str(kim)+"총급여:"+str(kim.getSalary()))