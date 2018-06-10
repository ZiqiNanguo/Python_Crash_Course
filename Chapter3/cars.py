# -*- coding: utf-8 -*-
"""
Created on Sun Jun  3 20:08:15 2018

@author: xinguang
"""
#list.sorted()会永久改变列表
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse = True)
print(cars)

cars = ['bmw', 'audi', 'toyota', 'subaru']

#sorted()不改变列表
cars = ['bmw', 'audi', 'toyota', 'subaru']
print("Here is the original list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars))

print("\nHere is the sorted list:")
print(sorted(cars,reverse = True))

print("\nHere is the original list again:")
print(cars)

#list.revierse() 反转列表元素的排列顺序
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)

cars.reverse()
print(cars)

#只要列表不为空，list【-1】始终是取最后一个元素
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles[-1])

'''
列表为空时，使用list【-1】会出错
motorcycles = []
print(motorcycles[-1])
'''