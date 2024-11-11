# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 10:33:01 2024

@author: Administrator
"""

import random

"""
x = random.random() #   0.0 <= x < 1.0 (범위 외우기)
print(x)

x = random.randint(1, 100)  #   a <= x <= b 
y = random.randint(1, 100)
print(x)
print(y)

"""  

count=0
answer=int(input("number:"))

while True:
   x = random.randint(1, 100)   
   y = random.randint(1, 100)
   print("x+y=",x+y)
   
   count+=1
   
   if answer == (x+y) : # input:78
       break
   #count+=1
   
print("count=", count)
#print("count=", count+1)

    