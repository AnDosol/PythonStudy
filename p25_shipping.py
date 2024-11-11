# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 14:05:06 2024

@author: Administrator
"""

country=input("배송지(현재는 korea와 us만 가능):") # 20000,3000
price=int(input("상품의 가격:"))

if country =="korea":
    
    if price >=20000:
        shipping_cost=0
    else:
        shipping_cost=3000
        
    
else:  # 100000,8000
    if price >=100000:
        shipping_cost=0
    else:
        shipping_cost=8000
        
print("배송비=",shipping_cost)