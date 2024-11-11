# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 09:20:23 2024

@author: Administrator
"""

# 0에서 99 중 10개의 숫자를 랜덤으로 출력
# a <= N <= b => randint()

import random


for i in range(10):
    rnd=random.randint(0, 99)
    print(rnd,end=" ")
print()


s="abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$^&*()?"
passlen=8
#p=random.sample(s,passlen)
#print(p)
p="".join(random.sample(s, passlen))
print("\n생성된 암호=", p)
print(type(p))
p2=random.sample(s,passlen)
print(p2)
print(type(p2))

# random.sample(sequence,k)
# sequence:list,set,range()
# k:반환될 리스트의 크기

my_string="abcdefg"
random_character=random.sample(my_string, 2)