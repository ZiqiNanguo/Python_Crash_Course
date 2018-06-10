# -*- coding: utf-8 -*-
"""
Created on Sun Jun  3 20:48:58 2018

@author: xingu
"""

banned_users = ['andrew', 'carolina', 'david']
user = 'marie'

if user not in banned_users:
    print(user.title() + ", you can post a response if you wish.")