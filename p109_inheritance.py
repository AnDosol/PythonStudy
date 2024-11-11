# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 16:06:57 2024

@author: Administrator
"""

import math

class Shape:
    def __init__(self):
        pass
    def draw(self):
        print("draw가 호출됨")
    def get_area(self):
        print("get_area()가 호출됨")
        
class Circle(Shape):
    def __init__(self,radius=0):
        self.radius=radius
        
    def draw(self): # override(재정의) => 아들꺼가 먼저 쓰임
        #super().draw()
        print("원을 그립니다.")
        
    def get_area(self):
        return math.pi*self.radius**2
    
c=Circle(10)
c.draw()
area=c.get_area()
print(area)
        
    