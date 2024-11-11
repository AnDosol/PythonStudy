# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 11:15:44 2024

@author: Administrator
"""

s="Monty Python"
print(s)
print(s[0],s[2])
# pyth
print(s[6:10]) # Pyth

print(s[-1])  # n (뒤부터)
print(s[-11]) # o (뒤에서)
print(s[-12]) # M (뒤에서)
# Monty
print(s[-12:-7])
# 모두 음수일 때는 끝의 수에 값을 +1 더한다.

numbers=[1,2,3,4,5,6,7,8,9,10]

reversed=numbers[:3] # 처음 ~ n-1
print(reversed)

reversed=numbers[:-3] # 처음 ~ n-1
print(reversed)

numbers=[1,2,3,4,5,6,7,8,9,10]

rever=numbers.reverse()
print(rever) # None

print(numbers.reverse())
print(numbers)
print(numbers.reverse())
print(numbers)

print(reversed(numbers))
# reverse 함수는 값을 반환하지 않는다

num=reversed(num_list)
print(list(num))

