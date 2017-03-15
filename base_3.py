# -*- coding: utf-8 -*-
"""
Created on Tue Mar 2017
@author: jiang
"""
place = ['wuhan','nanchang','chongqin','shanghai','beijing']
for tour in place:  #for循环遍历
    print (tour.title())
    print (tour.title() + ",That's a great place." )

print 'where you want to go ?'

number = list(range(1,6))   #创建数值列表
print (number)
even_number = list(range(2,13,2))
print (even_number)

squars = []
for value in range(1,11):
    square = value **2
    squars.append(square)   #可以直接改为squars.append(value**2)
print (squars)

dim = [1,2,3,4,5,6,7,8,9,0] #对数字列表进行简单统计计算
print (min(dim))
print (max(dim))
print (sum(dim))

lim = [value**2 for value in range(1,15)]   #列表解析
print (lim)
print (lim[1:3])
print (lim[:3])
print (lim[3:])
print (lim[-3:])
for num in lim[:3]:
    print (num)
lim_copy =lim[:]
print(lim_copy)

dimen = (200,50)    #元组的基本使用
print (dimen[0])
print (dimen[1])
for dimens in dimen:
    print (dimens)
