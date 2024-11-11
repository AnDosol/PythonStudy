# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 16:26:37 2024

@author: Administrator
"""

# 1부터 10까지의 합
# for, sum

def get_sum(start,end):
    
    sum=0
    
    
    for a in range(start, end+1):
        sum+=a
        
        return sum
        
def main():
    
    value=get_sum(1,10)
    print(value)
    