# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 10:12:59 2024

@author: Administrator
"""

price=int(input("상품의 가격 입력:"))

if price>20000:
    shipping_cost=0
    #print("배송비 =",shipping_cost)
    
else: 
    shipping_cost=3000
    #print("배송비 =",shipping_cost)
    
print("배송비=",shipping_cost)

if price > 100000:
    
    pass# 나중에 개발하겠다는 키워드
    
else:
    pass