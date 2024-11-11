# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 14:20:44 2024

@author: Administrator
"""

import turtle

t=turtle.Turtle()
t.shape("turtle")

s=turtle.textinput("사각형","도형을 입력하시오:")

if s == '사각형':
    w=int(turtle.textinput("", "가로"))
    h=int(turtle.textinput("", "세로"))
    
    t.forward(w)
    t.right(90)
    t.forward(h)
    t.right(90)
    t.forward(w)
    t.right(90)
    t.forward(h)
    
    
    
turtle.mainloop()
turtle.bye()