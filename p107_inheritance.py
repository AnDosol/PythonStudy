# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 14:11:47 2024

@author: Administrator
"""

class Car:
    def __init__(self,make,model,color,price):
        self.make=make
        self.model=model
        self.color=color
        self.price=price
        
    def setMake(self,make):
        self.make=make
    
    def getMake(self):
        return self.make
    
    def getDesc(self):
        
        return "차량=("+str(self.make)+str(self.model)+str(self.color)+str(self.price)+")"
    
class ElectricCar(Car):
   def __init__(self,make,model,color,price,batterySize):
       #self.make=make
       #self.model=model
       #self.color=color
       #self.price=price
       super().__init__(make,model,color,price)# 부모 생성자 호출
       self.batterySize=batterySize
       
       
   def setBatterySize(self,batterySize):
       self.batterySize=batterySize
       
   def getBatterySize(self):
       return self.batterySize
       
def main():
    myCar=ElectricCar("Teslla", "Model s", "White", 10000, 0)
    my=myCar.getMake()
    print(my)
    myCar.setMake("Tesla")
    my=myCar.getMake()
    print(my)
    myCar.setBatterySize(60)
    print(myCar.getDesc())
    
main()