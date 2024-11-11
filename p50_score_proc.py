# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 15:14:47 2024

@author: Administrator
"""
STUDENT=5
#STUDENT=7
#print(STUDENT)

lst=[]
count=0

for i in range(STUDENT): # 0~4(5-1)
    value=int(input("성적을 입력하세요:"))
    lst.append(value)
    
print("\n 성적평균",sum(lst)/len(lst))
print("최대 점수=",max(lst))
print("최소 점수=",min(lst))


for i in lst:
    if i >= 80: 
        count+=1
print("80점 이상은",count)        
        
        
    