# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 09:16:02 2024

@author: Administrator
"""

mydict={}

for i in range(3):
    date = input("날짜를 입력하시오:") # 2024 10 22, 2024 10 23
    job = input("일정을 입력하시오:") # 화요일 비오는 날, 공부하는 날

   # mydict[date]=job
    if date in mydict:
       #mydict[date].append(job)
       mydict.update({date:job})
       
       
    else:
       mydict[date]=[]
       mydict[date].append(job)
    
    
    
    
    
    
print(mydict)
