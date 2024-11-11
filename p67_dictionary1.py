# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 16:52:55 2024

@author: Administrator
"""

# dictionary => key : value
# key : 불변, 유일

capitals={
        "korea":"Seoul",
        "USA" : "Washington",
        "UK" : "London"        
        }

#print(capitals["Korea"])
#print(capitals["France"]) # KeyError: 'France'

message=capitals.get("France","해당 키가 없습니다.")
print(message)

capitals.update({
    "Germany":"Berlin",
    "Japan" : "Tokyo"    
    })
print(capitals)

city=capitals.pop("Japan")
print(city)
print(capitals)

capitals.clear()

print(capitals) 

if len(capitals) == 0:
    print("딕셔너리가 비어있음")
    
else:
    print("딕셔너리에 항목이 있음")