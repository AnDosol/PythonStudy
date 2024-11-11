# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 10:02:51 2024

@author: Administrator
"""
"""
english_dict={} # 공백 딕셔너리 생성
print(type(english_dict)) # <class'dict'>
english_dict["one"]="하나"
english_dict["two"]="둘"
english_dict["three"]="셋"

print(english_dict) # {'one': '하나}

word=input("단어를 입력하세요:")
print(english_dict[word]) 
"""


english_dict={} # 공백 딕셔너리 생성, 키와 값은 3개
count=0

while count < 3:
    key=input("키를 입력하세요:")    # 키입력
    value=input("값를 입력하세요:")    # 값입력
    english_dict[key]=value   # 입력받은 값을 딕셔너리에 저장
    count+=1    # count 증가

print(english_dict)
    