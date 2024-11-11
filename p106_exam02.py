# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 12:12:41 2024

@author: Administrator
"""

class Person():

    def __init__ (self,name,mobile=None,office=None,email=None):
        self.name=name
        self.mobile=mobile
        self.office=office
        self.email=email
        
    def setMobile(self,number):
        self.mobile=number
        
    def setoffice(self,number):
        self.office=number
        
    def setEmail(self,address):
        self.email=address
    def __str__(self):
        s=''
        s+=self.name+'\n'
        s+="mobile:"+self.mobile+'\n'
        s+="office phone:"+self.office+'\n'
        s+="email address:"+self.email+'\n'

        return s        
        
class PhoneBook():
    def __init__(self):
        self.contacts={}
        
    def add(self,name,mobile=None,office=None,email=None):
        p=Person(name,mobile,office,email)
        self.contacts[name]=p
        print(p)
        
    def __str__(self):
        s=''
        for p in sorted(self.contacts):
            print("p:",self.contacts[p])
            str(self.contacts[p])+'\n'
            
        return s
            
obj=PhoneBook()
obj.add('kim',mobile="010-1111-2222",office="1234567",email="kim@company.com")
obj.add('park',mobile="010-2222-3333",office="8901234",email="park@company.com")

print(obj)