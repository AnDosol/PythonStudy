# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 16:07:41 2024

@author: Administrator
"""

list1=[10,2,3,4,15,99]
list1.sort()
print(list1)

# 뒤에서 두 번재 요소를 출력
print("두 번째로 큰수",list1[-2])
list1.remove(list1[0])
list1.remove(list1[-1])

print(list1)

scores=[10.0,9.0,8.3,7.1,3.0,5.0]
print("score:",scores)
scores.sort()
print("score:",scores)

new_scores=scores[1:4] # 1:4-1
print("new_scores:",new_scores)

new_scores=scores[1:-1] 
print("new_scores:",new_scores)

print(list(range(10)))

print(list(range(0, 10)))

