# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 17:12:09 2024

@author: Administrator
"""

class BankAccount:
    def __init__(self):
        self.__balance=0
        
    def withdraw(self,amount):
        self.__balance-=amount
        print("통장에 ",amount,"가 출금되었음")
        return self.__balance
    
    def deposit(self,amount):
        self.__balance+=amount
        print("통장에 ",amount,"가 입금되었음")
        return self.__balance
    
a=BankAccount()
a.deposit(100)
a.withdraw(50)
print("a id=",id(a))

share=a # 객체 참조값 복사(공유)
share.deposit(100)
share.withdraw(50)
print("share id=",id(share))


