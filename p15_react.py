# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 16:25:38 2024

@author: Administrator
"""

import turtle # 모듈

t=turtle.Turtle()

t.shape("turtle") # arrow, circle, square, triangle

a=int(input("길이입력:"))
b=int(input("방향 값 입력:"))

t.forward(a) # 방향
t.left(b) # 각도
t.forward(a)
t.left(b) # 각도
t.forward(a)
t.left(b) # 각도
t.forward(a)


turtle.mainloop()
turtle.bye()