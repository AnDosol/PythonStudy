# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 16:54:23 2024

@author: Administrator
"""

# "Hi! I'm Park, and I'm form korea."
# "Hi! I'm sam, and I'm form USA."
# "Hi! I'm sakura, and I'm form Japan."
# "Hi! I'm guest"

studentList={
    "Park":"Korea",
    "Sam" :"USA",
    "Sakura" :"Japan" 
    }

def greeting(name):
    # if else
    
    if name in studentList:
        return "Hi! I'm "+name+", and I'm from "+studentList[name]+"."
    else:
        return "Hi! I'm guest"
    
print(greeting("Park"))
print(greeting("Sam"))
print(greeting("Sakura"))