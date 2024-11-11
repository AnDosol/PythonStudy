# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 11:47:10 2024

@author: Administrator
"""

import random

tries=0
guess=0
answer=random.randint(1, 100)

print("1부터 100사이의 숫자를 맞추세요.")


while True:
    
    guess=int(input("숫자를 입력하세요:"))    
    tries+=1

    if guess > answer:
        if guess-answer >10:
            print("너무 높음")
        elif guess-answer <10:
            if guess < answer:
                print("조금 높음")
            elif guess > answer:
                print("조금 낮음")
            
    
    elif guess < answer:
        if answer-guess >10:
            print("너무 낮음")
        elif answer-guess < 10:
            if guess < answer:
                print("조금 높음")
            elif guess > answer:
                print("조금 낮음")
            
    else:
        print("정답은:",answer,"시도 횟수:",tries)
        
        break
        