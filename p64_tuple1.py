# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 13:59:08 2024

@author: Administrator
"""

# 튜플(turple): 리스트와 같으나 변경이 불가능 하다
# 추가, 수정, 삭제 불가능

fruits=("apple","banana","grape")
result=fruits

print(result)
print(type(fruits))
print(type(result))

fru=["apple", "banana"]
fru[0]="kiwi"
print(fru)

#fruits[0]="kiwi"
#print(fruits)
#TypeError: 'tuple' object does not support item assignment

myList=[1,2,3,4]
myTuple=tuple(myList)
print(myTuple)
print(type(myTuple))
print(type(myList))

fruits2=("orange", "strawberry", "lemon")
#fruits2.append("pear")

# pear,kiwi추가를 하고 싶다(누적)
fruits2=fruits2+("pear","kiwi")
print(fruits2)

student=("kim",[3.1,3.6,4.0,0.0])
print(student)
print(student[0])
print(student[1])

flo=student[1][0]
print(flo)

#0.0 = > 4.3

student[1][3]=4.3
print(student)

print("-----------------------------------------------------")

x=("apple","banana","grape")
(s1,s2,s3)=x,x,x
print(s1,s2,s3)

# name, grade

name,grade=student
print(name) # kim
print(grade) # [3.1,3.6,4.0,4.3]

# 값 교환
n1=10
n2=20

n1,n2=n2,n1

print(n1)
print(n2)











































