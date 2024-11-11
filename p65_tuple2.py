# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 15:21:11 2024

@author: Administrator
"""

# 인덱스 값과 요소값 접근:enumerate()함수
# 반복 가능한 객체를 인자로 받아서 해당 객체의
# 요소들을 순회하면서 각 요소의 인덱스와 값을 
# 순서쌍으로 반환

fruits=["apple","banana","grape"]
print(fruits)
print(enumerate(fruits))

for index, value in enumerate(fruits):
    print(index,value)
    
#result1,result2=enumerate(fruits)
#print(result1, result2)

result=enumerate(fruits)

result=list(enumerate(fruits))
print(result)
print(type((0,'apple')))

print("============================집합=============================")
numbers=set([1,2,3,1,2,3])
print(numbers)

fruits2=("apple", "banana", "grape")
#fruits2.add("kiwi")
print(fruits2[0]) # apple

fruits3={"apple","banana","grape"}
print(fruits3)
#print(fruits3[0])

fruits3.add("kiwi")
print(fruits3)

#fruits3.remove("kiwi") # KeyError : 'kiwi'
fruits3.discard("kiwi") # 에러 발생 안함
print(fruits3)

fruits4={"apple","banana","grape","grape"}
print(fruits4)

fruits4.update(["orange","mango","mango","kiwi"])
print(fruits4)

# 합집합
a={"apple","banana","grape"}
b={"apple","banana","kiwi"}

c=a.union(b)
c=a|b
print("합집합:",c)

# 교집합
# c=a.intersection(b)
c=a&b
print('교집합:', c)

# 차집합
#c=a.difference(b)
c=a-b
print("차집합:",c)
c=b-a
print("차집합:",c)

























