# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 10:17:51 2024

@author: Administrator
"""

"""
자동차(설계도):클래스 ==> 자동차 완성(객체:object)
클래스:변수+함수
도어:3,4,5
색상:검정,회색,흰색
타이어:한국,금호,넥센
"""

# 클래스 이름의  첫글자는  일반적으로 대문자
class Counter:
    # 생성자(constructor) : 객체를 초기화하는 메서드
    # 클래스로 객체를 생성할 때 디폴트로 자동 호출
    def __init__(self):
        self.count=0
        
    def increment(self):
        self.count+=1
        print(self.count)
        
# 객체 생성
a=Counter()
print(a)
a.increment()     