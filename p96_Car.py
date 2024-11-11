# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 14:06:18 2024

@author: Administrator
"""

class Car:
    def __init__(self,speed,color,model):
        self.speed=speed
        self.color=color
        self.model=model
        
    def drive(self):
        self.speed=60
        
myCar=Car(0,"blue","E-class")

print("자동차 객체가 생성하였습니다.")

print("자동차의 속도는:",myCar.speed)
print("자동차의 색상은:",myCar.color)
print("자동차의 모델은:",myCar.model)

myCar.drive()# 자동차의 속도 변경
print("자동차의 속도는:",myCar.speed)
        
        