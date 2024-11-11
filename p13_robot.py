# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 15:16:51 2024

@author: Administrator
"""

# 경기장이 어디입니까? 안산(키보드로부터 입력)
stadium=input("경기장이 어디입니까?")
winner=input("이긴팀이 어디입니까?")
loser=input("진팀이 어디입니까?")
vip=input("우수 선수는 누구입니까?")
score=input("스코어는 몇 대 몇 입니까?")

print()
print("========================================================")
print("오늘",stadium,"에서 야구 경기가 열렸습니다.")
print(winner,"과",loser,"은 치열한 공방전을 펼쳤습니다.")
print(vip,"이 맹활약을 하였습니다.")
print("결국",winner,"가",loser,"를",score,"로 이겼습니다.")