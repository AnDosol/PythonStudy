# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 12:18:16 2024

@author: Administrator
"""

#list(자료구조)
temps=[28,31,33,35,27,26,25]
print(temps[3])
e=temps[3]
print("e=",e)
# print(temp[7]) # IndexError: list index out of
# 0~6
print(temps[-1]) # 25
print(temps[-2]) # 26

print("length temps=", len(temps))

for i in temps:
    print(i,end=",")
print("\n")

for i in range(len(temps)): #
    print(temps[i])

