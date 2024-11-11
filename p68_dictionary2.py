# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 17:10:45 2024

@author: Administrator
"""

capitals={
        "korea":"Seoul",
        "USA" : "Washington",
        "UK" : "London"        
        }

for key in capitals:
    #print(key) # Korea USA UK
    print(key,":",capitals[key])

"""
for key, value in capitals:
    print(key)
    print(value)
"""    
for key,value in capitals.items() :
    print(key,":",value)
    
    
print(type(key)) # str
print(type(value)) # str

dic={i:str(i)for i in [1,2,3,4,5]}
print(dic) # {1: '1', 2: '2', 3: '3', 4: '4', 5: '5'}
print(type(dic)) # <class 'dict'>

fruits=["apple","orange","banana"]
dic={f:len(f) for f in fruits}
print(dic)

print("=================================================================")

dic1={"one":1,"Two":2,"Three":3}
print(dic1)
print(dic1["one"]) # 1
# 1 => 10
dic1["one"] = 10
print(dic1["one"])

dic2={w:n for w,n in dic1.items()}
print(dic2)
print(dic2.keys())
print(dic2.values())    
    
    
    