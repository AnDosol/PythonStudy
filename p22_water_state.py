# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 11:17:15 2024

@author: Administrator
"""

temp=float(input("온도를 입력하세요:"))


if  temp <= 0:    
    print("물의 상태는 얼음입니다.")

elif 0 < temp < 100:
    print("물의 상태는 액체입니다.")

else:
    print("물의 상태는 기체입니다.")