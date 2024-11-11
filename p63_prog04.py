# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 12:40:05 2024

@author: Administrator
"""

# 2개의 리스트를 받아서 공통 구성원이 하나 이상 있으면
# True를 없으면 False 반환하는 프로그램
# for, if

s1=[1,2,3,4,5,6]
s2=[11,7,8,9,1]



def common_data(a,b):
    
    c=False
    
    for i in range(len(a)):
        for j in range(len(b)):
            if a[i]==b[j]:
            
                c=True
                
                return c
            
            
            
            
print("list1=",s1)
print("list2=",s2)
print(common_data(s1,s2))