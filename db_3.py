# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 16:23:30 2024

@author: Administrator
"""

import pymtsql
from tkinter import*
from tkinter import messagebox

def insertData():
    conn, cur=None,None
    data1, data2, data3, data4="","","",""
    sql=""
    
    conn=pymysql.connect(host='127.0.0.1',user='root',password='1234',db='hanjikgyo',charset='utf8')
    cur=conn.cursor()
    
    data1=edit1.get()
    data2=edit2.get()
    data3=edit3.get()
    data4=edit4.get()
    
    try:
        sql="insert into userTable values('"+data1+"','"+data2+"','"+data3+"','"+data4+"')"
       
        cur.execute(sql)
    except:
        messagebox.showerrer('오류', '데이터 입력 오류가 발생')
    else:
        messagebox.showinfo('성공','데이터 입력 성공')
        
    conn.commit()
    conn.close
    
def selectData():
    strData1,strData2,strData3,strData4=[],[],[],[]
    
    conn=pymysql.connect(host='127.0.0.1',user='root',password='1234',db='hanjikgyo',charset='utf8')
    cur=conn.cursor()
    
    cur.execute("select * from userTable")
    strData1.append("사용자ID")
    strData2.append("사용자 이름")
    strData3.append("이메일")
    strData4.append("출생년도")
    strData1.append("--------------")
    strData2.append("--------------")
    strData3.append("--------------")
    strData4.append("--------------")
    
    while(True):
        row=cur.fecthone()
        if row == None:
            break;
            
        strData1.append(row[0])
        strData2.append(row[1])
        strData3.append(row[2])
        strData4.append(row[3])
        
        listData1.delete(0,listData1.size()-1)
        listData2.delete(0,listData2.size()-1)
        listData3.delete(0,listData3.size()-1)
        listData4.delete(0,listData4.size()-1)
        
    for item1,item2,item3,item4 in zip(strData1,strData2,strData3,strData4):
        listData1.insert(END,item1)
        listData2.insert(END,item2)
        listData3.insert(END,item3)
        listData4.insert(END,item4)
    
    conn.close
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    