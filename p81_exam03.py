# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 14:21:41 2024

@author: Administrator
"""

d={
  1:10,
  2:20,
  3:30,
  4:40,
  5:50,
  6:60 
  }

def is_key_present(x):
    
    
    if x in d:
        print(f"키 {x}가 딕셔너리에 있습니다.")
       
    else:
        print(f"키 {x}가 딕셔너리에 없습니다.")
    
key=int(input("키를 입력하세요:"))
is_key_present(key)# 함수호출







