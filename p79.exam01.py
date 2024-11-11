# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 13:33:57 2024

@author: Administrator
"""

# 정수 리스트 중복 제거, 리스트 정렬
# set(집합):순서가 없고 unique한 값

def unique_sort(lst):
    
     
    return sorted(set(lst))

lst=[80,20,20,30,60,30]
print("주어진 리스트",lst)

newLst=unique_sort(lst)
print("정렬된 리스트",newLst)
