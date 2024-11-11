# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 16:13:26 2024

@author: Administrator
"""

def main():
    result=get_area(3)
    print("반지름이 3인 원의 면적=", result)
    
    return result
    
def get_area(radius):
    
    area=3.14*radius**2
    
    return area

result=get_area(3)
print("반지름이 3인 원의 면적=",result)

result2=get_area(20)
print("반지름이 20인 원의 면적=",result2)