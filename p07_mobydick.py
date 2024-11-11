# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 11:37:58 2024

@author: Administrator
"""

from collections import Counter

f=open("c://Python-Workspace-20240911//mobydick.txt",encoding="utf-8")
count=Counter(f.read().split())
print("단어 출현 회수:",count) # 개수