# -*- coding: utf-8 -*-
"""
Created on Sun Jun  3 19:50:45 2018

@author: xingu
"""

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
#修改列表元素
motorcycles[0] = 'ducati'
print(motorcycles)

#列表末尾添加元素
motorcycles.append('ducati')
print(motorcycles)

#列表中插入元素
motorcycles.insert(0, 'ducati')
print(motorcycles)

#从列表中删除元素
#使用del语句删除元素
del motorcycles[0]
print(motorcycles)

#使用pop()删除元素
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

motorcycles = ['honda', 'yamaha', 'suzuki']
last_owned = motorcycles.pop()
print("The last motorcycle I owned was a " + last_owned.title() + ".")

#弹出列表中任何位置处的元素
motorcycles = ['honda', 'yamaha', 'suzuki']
first_owned = motorcycles.pop(0)
print('The first motorcycle I owned was a ' + first_owned.title() + '.')

#根据值删除元素
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print("\nA " + too_expensive.title() + " is too expensive for me.")