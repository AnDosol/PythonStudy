# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 09:24:04 2024

@author: Administrator
"""

# 사용자로부터 4자리의 정수를 입력받아서
# 자리수의 합을 계산하는 프로그램
# 1234 => 1+2+3+4 => 10
# // : 몫, % : 나머지
"""
s=int(input("4자리 정수를 입력하세요:")) #1234

n=s%10 #4
s=s-n #1230
s=s//10 #123

n1=s%10 #3
s=s-n1 #120
s=s//10 #12

n2=s%10 #2
s=s-n2 #10
s=s//10 #1

n3=s

print("각 자리수의 합은 ",n+n1+n2+n3,"입니다.")
"""
n=int(input("정수 4자리 입력:"))
s=0

s+=n%10
n//=10
s+=n%10
n//=10
s+=n%10
n//=10
s+=n%10

print(s)