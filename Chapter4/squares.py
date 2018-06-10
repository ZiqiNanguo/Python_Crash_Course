# -*- coding: utf-8 -*-
"""
Created on Sun Jun  3 20:24:26 2018

@author: xinguang
"""

squares = []
for value in range(1,11):
    square = value**2
    squares.append(square)
    
print(squares)

squares = [value**2 for value in range(1,11)]
print(squares)