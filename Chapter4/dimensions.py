# -*- coding: utf-8 -*-
"""
Created on Sun Jun  3 20:37:11 2018

@author: xingu
"""

dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

"""元组不能直接赋值
dimensions[0] = 250
"""

dimensions = (200, 50)
for dimension in dimensions:
    print(dimension)
    
dimensions = (200, 50)
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)
dimensions = (400, 100)#实际上重新定义了一个元组
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)