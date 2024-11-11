# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 12:25:21 2024

@author: Administrator
"""

problems={
    "파이썬" : "최근에 가장 떠오르는 프로그래밍",
    "변수" : "데이터를 저장하는 메모리 공간",
    "함수" : "작업을 수행하는 문장들의 집합에 이름을 붙인 것",
    "리스트" : "서로 관련이 없는 항목들의 모임"   
    }

def show_words(problems):
    display_message=""
    i=1
    for word in problems:   #key값만 반환
      #  print(word)
        display_message += "("+str(i)+")"
        display_message += word+" "
        i+=1
    print(display_message)


for meaning in problems.values():        
    print("다음은 어떤 단어에 대한 설명일까요?")       
    print("\""+meaning+"\"")
    
    correct=False        
        
    while not correct:
        show_words(problems)
        guessed_word=input()
        if problems[guessed_word] == meaning:
            print("정답")
            correct=True
        else:
            print("오답")
        
show_words(problems)










