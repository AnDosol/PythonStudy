# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 11:35:09 2024

@author: Administrator
"""

#1부터 100사이의 난수 10개를 생성하여 리스트에 저장
#for, random, append
#randdomList리스트에 저장

import random

randdomList=[]



for i in range(10):
    a=random.randint(1,100 )
    randdomList.append(a)
    
print(randdomList)