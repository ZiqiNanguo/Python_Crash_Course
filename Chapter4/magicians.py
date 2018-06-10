# -*- coding: utf-8 -*-
"""
Created on Sun Jun  3 20:18:22 2018

@author: xinguang
"""

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)
    
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician.title() + ", thas was a great trick!")
    print("I can't wait to see your next trick, " + magician.title() + ".\n")
print("Thank you, everyone. That was a great magic show!")