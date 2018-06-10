# -*- coding: utf-8 -*-
"""
Created on Sun Jun  3 17:36:31 2018

@author: xinguang
"""

name = "ada lovelace"
print(name.title()) #name.title() 使每个单词首字母改为大写

name = "Ada Lovelace"
print(name.upper()) #name.upper() 使全部单词为大写
print(name.lower()) #name.lower() 使全部单词为小写

#连接字符
first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name

message = "Hello, " + full_name.title() + "!"
print(message)

#删除空白
favorite_language = 'python '
print(favorite_language)
 #删除结尾空白
print(favorite_language.rstrip())

favorite_language = ' python '
print(favorite_language)
print(favorite_language.lstrip()) #删除开头空白
print(favorite_language.strip()) #删除两端空白