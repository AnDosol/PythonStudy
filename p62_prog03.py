# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 12:11:05 2024

@author: Administrator
"""

#"aba"처럼 첫 번째 문자와 마지막 문자가 동일한
#문자열 수를 계산하는 프로그램
#for if and len()



def match_words(words):
    pass
    a=0

    for i in range(len(words)):
     
     if len(words) > 1 and words[i][0]==words[i][-1]:
         a+=1
    
   
    return a     


s=['aba', 'xyz', 'abc', '121', 'aa', 'a']
match_words(s)
print(s)
print("문자열의 개수=",match_words(s))


"""
def match_words(words):
    pass
    a=0

    for word in range(words):
     
     if len(word)>1 and word[0] == word[1]
         a+=1
    return a 
""" 