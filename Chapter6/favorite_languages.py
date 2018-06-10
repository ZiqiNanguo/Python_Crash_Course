# -*- coding: utf-8 -*-
"""
Created on Sat Jun  9 09:43:33 2018

@author: xingu
"""

favorite_languages = {
        'jen':'python',
        'sarah':'c',
        'edward':'ruby',
        'phil':'python',
        }
for name,language in favorite_languages.items():
    print(name.title() +"'s favorite language is " + 
          language.title() + ".")