# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 14:27:03 2024

@author: Administrator
"""

squares=[]

for x in range(10): # 0,1,2,3,4,5,6,7,8,9
    squares.append(x*x)
    
print(squares)

# [0,1,4,9,16,25,36,49,64,81]

# 리스트 함축(List comprehension)


squares=[(x*x)for x in range(10)]

print(squares)

# 0부터 9사이의 정수 중 짝수만을 제곱한 값을 리스트 함
squares=[(x*x)for x in range(10)if x%2 == 0]
print(squares) # [0,4,16,36,64]

prices=[135,-545,922,356,-992,217]
#mprices=[i for i in prices if x>0 else 0]
mprices=[i if i>0 else 0 for i in prices]
print(mprices)

words=["all","good","things","must","come","to","an","end"]
print(words)
#for w in words:
#    print(w)

letters=[w for w in words]
print(letters) # ['all', 'good', 'things', 'must', 'come', 'to', 'an', 'end']

#['a','g','t','m','c','a','e']
letters=[w[0] for w in words]
print(letters)

for w in words:
# agtmctae
    print(w[0], end="") 
    
print('\n')

for w in words:
    print(list(w))
    
print('\n')    
    
for w in words:
    print(list(w[0]))

print('\n')     

for w in words:
   a=list(w[0])
   print(a)
print("==========================================================")

letter4=[]
for w in words:
   
   letter4.insert(1,w[0])
   print(letter4)    

print("==========================================================")
for x in ['a','b','c']:
    for y in ['x','y','z']:
        
        q=x+y
        
        print (list(q[0]),end="")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    