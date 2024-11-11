# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 17:09:08 2024

@author: Administrator
"""
"""
def sub(x,y,z):
    print('x=',x,'y=',y,'z=',z)
    
sub(10,20,30)
sub(z=30,y=20,x=100)
"""

def varfunc(*args):
    print(args)
    
print("하나의 값으로 호출")
varfunc(10)
print("여러개의 값으로 호출")
varfunc(10,20,30)