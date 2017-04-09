# -*- coding: utf-8 -*-
"""
Created on Tue Mar 2017
@author: jiang
"""
def sqare_sum(a,b):
    c = a**2 + b**2
    return c
print ("the sqare is:" + str(sqare_sum(3,4)))

def make_piza(*topings):   #创建一个名为toping的元组
    """打印顾客点的所有配件"""
    for msg in topings:
        print (msg.title())

make_piza('orange')
make_piza('pear','banana','apple')

def make_pai(size,*topings):
    """概述要制作的pai"""
    print ("\nMaking a "+ str(size)+ "-inch pizza with the following topings:")
    for toping in topings:
        print ("- "+ toping.title())

make_pai(16,'boat')
make_pai(12,'banana','strawberry','apple')

def build_profit(first,last,**user_info):  #创建名为user_info的字典。 
    """创建一个字典，其中包含用户的所有信息"""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key,value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profit('jiang','zheng',location = 'nanchang',school = 'ECJTU')
print(user_profile)
