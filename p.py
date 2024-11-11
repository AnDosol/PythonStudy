# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 15:53:23 2024

@author: Administrator
"""

import pymysql

conn,cur=None,None
data1,data2,data3,data4="","","",""
sql=""

conn=pymysql.connect(host='127.0.0.1',user='root',password='1234',db='hanjikgyo',charset='utf8')
cur=conn.cursor()
sql="create table if not exists userTable(id char(4),userName char(15),email char(20), birthYear int)"
cur.execute(sql)

while(True):
    data1=input("사용자 ID ==>")
    if data1 == "":
        break
    data2=input("사용자 이름 ==>")
    data3=input("사용자 이메일 ==>")
    data4=input("사용자 출생년도 ==>")
    sql2="insert into userTable values('"+data1+"','"+data2+"','"+data3+"','"+data4+"')"
   
    cur.execute(sql2)
   
conn.commit()
conn.close()