# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 12:44:02 2024

@author: Administrator
"""

import turtle

t=turtle.Turtle()
t.shape("turtle")

t.width(3) # 선의 두께
t.shapesize(3,3) # (너비, 길이)

while True:
     command=input("명령을 입력하시오:")
     # l: left r: right q:quit
     # forward:100
     # 각도:90(left, right)
     # if(l,r,q)
     
     if command =='l':
         t.left(90) # 각도
         t.forward(100)
     if command =='r':
         t.right(90)
         t.forward(100)
     if command =='q':
         break
    
turtle.mainloop()
turtle.bye()