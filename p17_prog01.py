# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 17:11:54 2024

@author: Administrator
"""

#x,y,z : 닭다리 2개, 돼지다리 4개, 소다리 4개
# 닭의 수, 돼지의 수, 소의 수

x=int(input("닭의 수를 입력하세요:"))
y=int(input("돼지의 수를 입력하세요:"))
z=int(input("소의 수를 입력하세요:"))

print("닭의 수는"+str(x)+"이고,","다리의 수는"+str(x*2)+"개 입니다.")
print("돼지의 수는"+str(y)+"이고,","다리의 수는"+str(y*4)+"개 입니다.")
print("말의 수는"+str(z)+"이고,","다리의 수는"+str(z*4)+"개 입니다.")

print("전체 다리의 수:",x*2+y*4+z*4)