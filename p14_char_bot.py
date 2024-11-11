# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 15:46:01 2024

@author: Administrator
"""

print("안녕하세요?")
name=input("이름이 어떻게 되나요?")# 이름이 어떻게 되나요?
print("만나서 반갑습니다."+name+"씨")# 만나서 반갑습니다 + 이름

print("이름의 길이는 다음과 같군요:",len(name))

# input()입력되는 타입은 string, 중요

age=int(input("나이가 어떻게 되나요?"))
print("내년이면 ",age+1,"살이 되는 군요.")
print("내년이면 "+str(age+1)+"살이 되는 군요.")