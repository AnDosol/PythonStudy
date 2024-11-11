# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 16:59:18 2024

@author: Administrator
"""

weight=float(input("몸무게를 kg단위로 입력하세요:"))
height=float(input("키를 cm 단위로 입력하세요:"))

height=height/100
bmi=(weight/(height**2))
print("BMI 지수는"+str(bmi)+"입니다.")
