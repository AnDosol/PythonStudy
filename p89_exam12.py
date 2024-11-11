# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 16:09:34 2024

@author: Administrator
"""

#isalpha(): # 공백, 숫자 제외 bool(True, False)
#isdigit():# 숫자로만 구성된 문자열, 문자가 하나라도 있으면 False
#isnumberic(): #숫자값 표현에 해당하는 문자열"123"

def count_all(txt):
    
    return {
            "LETTERS": sum(1 for x in txt if x.isalpha()),
            "DIGIT": sum(1 for x in txt if x.isdigit()),
        }

print(count_all("Hello World123"))

a="½" # ㅊ+한자
print(a.isdigit()) # False
print(a,isnumeric()) # True