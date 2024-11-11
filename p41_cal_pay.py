# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 17:15:27 2024

@author: Administrator
"""
# 시급 1.5배, 30시간 초과
def weeklyPay(rate,hour):
    money=0
    
    if(hour > 30):
        money=rate*30+(rate*(hour-30)*1.5)
        
    else:
        money=rate*hour
        
    return money
    

rate = int(input("시급을 입력하세요:"))
hour = int(input("근무 시간을 입력하세요:"))

print("월급은"+str(weeklyPay(rate,hour)))