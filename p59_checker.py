# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 10:20:37 2024

@author: Administrator
"""

table=[]
#for row in range(10):
    #print(row) # 0~9
    #table+=[[0]]
    #table+=[[0]*0]
    #table+=[[0]*1]
    #table+=[[0]*row]
    
#print(table)

def printList(myList):
    for row in range(len(myList)): # 0~9
        for col in range(len(myList[0])): # 0~9
          print(myList[row][col],end="")

def init(myList):
    #pass
    for row in range(len(myList)): # 0~9
        for col in range(len(myList[0])): # 0~9
            if(row+col) % 2 == 0:
                myList[row][col]=1
                
   
        

for row in range(10):
    table+=[[0]*10] # 10행 10열
    
init(table)
printList(table)
