# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 09:23:21 2024

@author: Administrator
"""

def sub():
    
    return 1,2,3

a,b,c=sub()
print(a,b,c)

def print_birthday(name):
    

    print(name+"님 생일을 축하합니다.")    
    
    
print_birthday("홍길동")

def get_info():
        name=input("이름")
        age=int(input("나이"))
        
        return name, age

st_name,st_age = get_info()

print("이름은"+st_name+"이고 나이는 "+str(st_age)+"살 입니다.")