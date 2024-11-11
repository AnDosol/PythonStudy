# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 09:18:29 2024

@author: Administrator
"""

s=[
   [1,2,3,4,5],
   [6,7,8,9,10],
   [11,12,13,14,15]
  ]

print(s)
print(id(s))

rows=3
cols=5

s=[]
for row in range(rows): # 0~2
    s+=[0]*cols
    
print("s=", s) 

s=[
   [1,2,3,4,5],
   [6,7,8,9,10],
   [11,12,13,14,15]
  ]

rows=len(s)
print("rows=",rows)
cols=len(s[0])
print("cols=",cols)
print(s[0]+s[1]+s[2])

for r in range(rows):
    for c in range(cols):
        print(s[r][c],end="")
    print("")
    
i=0 # 행
total=0

for i in range(5):# 1행의 합, for range
    total+=s[0][i]
print(total)

# 2열의 합 for range

j=1
total=0

for j in range(3):
    total+=s[j][1]
print(total)





































