# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 11:06:58 2024

@author: Administrator
"""
"""
address_book={}

def main():
    #pass
    
    while True:    
        user=display_menu()
        if user == 1:
            name,number = get_contact()
            address_book[name]=number
    
        elif user == 2:
            name,number = get_contact()
            address_book.pop(name)
        
        elif user == 3:
            name,number = get_contact()
            get_search(name, number)
        
        elif user == 4:
            for key in address_book:
                print(key,"의 전화번호:",address_book[key])
        else:
        
                break
    

def display_menu():
    print("1:연락처 추가")
    print("2:연락처 삭제")
    print("3:연락처 검색")
    print("4:연락처 출력")
    print("5:종료")
    
    select=int(input("해당 항목을 선택하세요:"))
    
    return select
    
def get_contact():
    #pass
    name=input("이름:")    
    number=input("전화번호:")    
    
    return name, number
    
def get_search(name,number):
    #pass
   for key in address_book:
        
        if key==name and address_book.get(key)==number:
            print(name,"의 전화번호는",number,"입니다.")
            return  
        
   print("해당하는 연락처가 없습니다.")
    
main()
"""

list=[0,1,2,3,3,4,5,6,7,3]
list.remove(3)
print(list)

#list.del[4]
del list[4]
print(list)








































        