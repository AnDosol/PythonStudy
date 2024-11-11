# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 11:59:51 2024

@author: Administrator
"""

import random

print("동전 던지기 게임을 시작합니다.")

coin=random.randrange(2) # 0부터 n-1 (3) => 0,1,2
#print(coin)

if coin==0:
    print("앞면입니다.")
    
elif coin == 1:
    print("뒷면입니다.")
    
print("게임이 종료되었습니다.")
print("coin=",coin)

coin2=random.randrange(1,8,3)
print("coin2=",coin2)
