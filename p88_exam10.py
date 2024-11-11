# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 14:48:54 2024

@author: Administrator
"""
"""
문자열을 입력하시오:python java c
금칙어를 입력하시요:java
python **** c
"""
"""
f=input("금칙어를 입력하시오:") # java
print(f)
print(type(f))

f=input("금칙어를 입력하시오:").split() # java
print(f)
print(type(f))
"""




"""
def censor_string(txt,lst,character):
    #for, replace, len
    for word in lst:
        print(word) #java
        print(txt) #python C
        txt=txt.replace(word, character*len(word))
        print(txt)
    return txt
        
        
s=input("문자열을 입력하세요:") # python java C
f=input("금칙어를 입력하세요:").split() #java


print(censor_string(s, f, "*"))        
"""

for word in "java":
    print(word.replace(word, '*'),end="")
    
    print(word.replace(word, '*'*len(word)),end="")

a=['a', 'b', 'c']
print(a)

a1="abc"
print(a1)
print(type(a1))

print(a1.split())
print(type(a1.split()))












































