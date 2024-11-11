# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 11:46:19 2024

@author: Administrator
"""

class Television:
    def __init__(self,channel,volume,on):
        self.channel=channel
        self.volume=volume
        self.on=on
        
    def show(self):
        print(self.channel,self.volume,self.on)
        
    def setChannel(self,channel):
        self.channel=channel

    def getChannel(self):
        return self.channel
        
t=Television(9,10,True)

t.show()

t.setChannel(11)
cha=t.getChannel()
print("channel:",cha)

"""
def func(a=0,b=0):
    a=a
    b=b
    print(a)
    print(b)
    
func()
"""