# -*- coding: utf-8 -*-
"""
Created on Tue Jul 26 14:39:11 2016

@author: Jiang
"""
number =float(raw_input('Please input a value:'))
low = 0
high = number

guess = (high + low )/ 2

while abs(guess ** 2 - number) > 1e-5 :
    if guess ** 2 > number:
        high = guess
    else:
        low = guess
    guess = (high + low )/ 2
print 'The root of number is :' , guess
    
            
