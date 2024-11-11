# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 09:17:30 2024

@author: Administrator
"""

from random import randint

#print(randint(1,3)) # 1 or 2 or 3 random

computer=randint(1,3)

player=int(input("선택하세요:(1:가위 2:바위 3:보)"))

if computer == player:
    print("비겼음")
    
    
elif computer>player:
    if computer==3 and player==2:
        print("컴퓨터가 이겼음")
    elif computer == 3 and player ==1:
        print("사용자가 이겼음")
    elif computer == 2 and player == 1:
        print("컴퓨터가 이겼음")
        
elif computer<player:
    if computer==2 and player==3:
        print("사용자가 이겼음")
    elif computer == 1 and player ==3:
        print("컴퓨터가 이겼음")
    elif computer == 1 and player == 2:
        print("사용자가 이겼음")        

print("컴퓨터 : ",computer)
print("사용자 : ",player)