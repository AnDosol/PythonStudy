# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 15:09:38 2024

@author: Administrator
"""

colors=["red","orange","blue"]
values=["#FF0000","#008000","#0000FF"]

for a in zip(colors,values):

    print(a)
    
color_dictionary=dict(zip(colors,values))
print(color_dictionary)

# enumerate():인덱스값을 포함하여 반환, 순서 개념
# 이터레이터(Iterator):순서대로 다음 값을 리턴 할 수 있다.
# 자체적으로 next()함수를 내장하고 있다

myDict={}

for i,a in enumerate(colors):
    print(i,":",a)
    myDict[a]=values[i]
    
print(myDict)