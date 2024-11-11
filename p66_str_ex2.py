# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 16:22:41 2024

@author: Administrator
"""

# 입력 테스트
# I have a dream that one day every valley
# shall be exalted and every hill and mountain shall be made low

txt=input("입력테스트:")
words=txt.split(" ") # 분리 후 리스트 반환
print(words)

print(len(words))

unique=set(words)
print("사용된 단어의 개수=",unique) # 중복 단어 제거하고 나열
print("사용된 단어의 개수=",len(unique)) # 중볻 단어 제거하고 개수