# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 14:53:03 2024

@author: Administrator
"""

myDict={
        "옷":100,
        "컴퓨터":2000,
        "모니터":320
        }

print("총합계=",(myDict["옷"])+(myDict["컴퓨터"])+(myDict["모니터"]),
      sum(myDict.values()))

