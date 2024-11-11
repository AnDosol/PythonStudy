# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 15:00:52 2024

@author: Administrator
"""

import random

numbers=[10,3,7,1,9,4,2,8,5,6]
ascending_numbers=sorted(numbers) # 크기순으로 정렬된 새로운 리스트
print(ascending_numbers)
print(numbers) # 원본 변화 없음

print("합=", sum(numbers))
print("최대값=",max(numbers))
print("최소값=",min(numbers))
print("랜덤하게 선택한 항목=",random.choice(numbers))