# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 13:48:03 2024

@author: Administrator
"""

import math

class Circle:
    def __init__(self, radius):
        self.radius=radius
        
    def getArea(self):
        return math.pi*self.radius*self.radius

    def getPerimeter(self):
        return 2*math.pi*self.radius

# 객체생성
a=Circle(10)
print("10의 면적",a.getArea())
print("원의 둘레",a.getPerimeter())        
