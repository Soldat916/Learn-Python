# -*- coding: utf-8  -*-
"""
Created on Tue Mar 2017
@author:jiang
"""
bicycles = ['treak','cannondale','redline','specialized']   #定义列表
print (bicycles)        #打印输出
print (bicycles[0])     #打印输出列表第一个元素,注意索引从0开始
print (bicycles[-1])    #打印输出倒数第一个元素

message = 'My first bicycles was a ' + bicycles[0].title() + '.'    #字符串结合操作
print (message)

bicycles[0] = 'ducati'  #修改列表元素    
print (bicycles)

bicycles.append('bmw')  #列表末尾添加元素
print (bicycles)
bicycles.insert(0,'nicolai')    #列表开头位置添加元素
print (bicycles)

del bicycles[0] #删除列表开头元素,但无法再继续访问
print (bicycles)

pop_bicycle = bicycles.pop()    #默认删除列表处元素,可删除任意位置元素
print (pop_bicycle)
print (bicycles)

bicycles.remove('ducati')   #根据值删除列表元素
print (bicycles)

bicycles.append('adi')
print (sorted(bicycles))    #按照字母大小的顺序显示列表
print (sorted(bicycles,reverse=True))   #与字母相反的顺序显示列表
print (bicycles)
bicycles.sort() #按照字母大小对列表进行永久排序
print (bicycles)
bicycles.reverse()  #翻转列表元素的排列顺序
print (bicycles)

long = len(bicycles) #确定列表长度
print (long)
