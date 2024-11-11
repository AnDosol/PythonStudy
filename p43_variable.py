# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 09:38:57 2024

@author: Administrator
"""
"""
x=400
def myfunc():
    x=200
    print(x) # 200
    
def main():
    x=100
    print(x) # 100
    
myfunc()
main()

def myfunc():
    x=300
    print(x) # 200
    
def main():
    x=150
    print(x) # 100
    
myfunc()
main()
"""

gx = 100 # 전역 변수

def myfunc():
    global gx # 전역 변수를 사용하겠다
    gx=500 # 지역 변수
    print(gx) # 지역 변수 우선 500
    
myfunc()
print(gx) # 100 => 500(전역 변수 적용)