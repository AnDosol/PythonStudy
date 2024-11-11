# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 17:19:15 2024

@author: Administrator
"""

menu=0
friends=[]

while menu !=9:
    print("--------------------")
    print("1.친구 리스트 출력")
    print("2.친구 추가")
    print("3.친구 삭제")
    print("4.친구 이름 변경")
    print("9.종료")
    
    menu=int(input("메뉴를 선택하시오:"))
    
    if menu == 1:
        print(friends)
    elif menu == 2:
        name=input("이름을 입력하세요:")
        friends.append(name)
    elif menu == 3:
        del_name=input("삭제하고 싶은 이름을 입력하세요:")
        if del_name in friends:
            friends.remove(del_name)
        else: 
            print("이름이 발견되지 않았음")
    elif menu == 4:
        old_name=input("변경하고 싶은 이름을 입력하세요:")
        # 기존 이름을 찾는다, 새로운 이름을 입력 받는다
        # 새로운 이름을 기존이름 위치에 넣는다
        """
        index_number=friends.index(old_name)
        new_name=int("새로운 이름을 입력하세요:")
        friends.insert(index_number,new_name)
        friends.remove(old_name)
        """    
            #1. 변경하고자 하는 이름을 찾는다 만일 있다면
            #2. 해당되는 위치를 찾는다 없으면"이름이 발견되지 않았음"이라고 출력
            #3. 새로운 데이터를 입력받아 해당 기존이름 위치에 넣는다
            
        if old_name in friends:
            index_number=friends.index(old_name)
            new_name=input("새로운 이름을 입력하세요:")
            friends[index_number]=new_name
        else:
            print("이름이 발견되지 않았습니다.")
            
        
    else:
        break