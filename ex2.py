# -*- coding: utf-8 -*-
"""
Created on Sun Jul 24 22:23:51 2016

@author: Jiang
"""
import math

a = float(raw_input('Input a: '))
b = float(raw_input('Input b: '))
c = float(raw_input('Input c: '))
if a != 0:
    delta = b ** 2 - 4 * a * c
    if delta < 0:
        print 'No soliutions'
    elif delta == 0:
        s = -b/(2 * a )
        print 's:', s
    else:
        root = math.sqrt(delta)
        s1 = (-b + root)/ (2 * a)
        s2 = (-b - root)/ (2 * a)
        print 'Two distinct solutions are :', s1, s2
