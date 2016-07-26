# -*- coding: utf-8 -*-
"""
Created on Tue Jul 26 14:39:11 2016

@author: Jiang
"""

value = int(raw_input('Please input a number:'))

while value != 1:
    if value % 2 :
        value = value * 3 + 1
    else:
        value = value / 2
        print value
