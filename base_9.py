# -*- coding: utf-8 -*-
"""
Created on Mon April 2017
@author: jiang
"""
try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")
"""
测试样例
filename = "jiang.txt"
try:
    with open(filename) as f_obj:
        contents = f_obj.read()
except FileNotFoundError: 
    msg = "Sorry ,the file " + filename +" does's exist."
    print(msg)
else:
    words = contents.split()
    num_words = len(words)
    print ("The file "+ filename + " has about " + str(num_words)+" words.")
"""

def count_words(filename):
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError: 
        msg = "Sorry ,the file " + filename +" does's exist."
        print(msg)
    else:
        #计算文件包含多少个单词
        words = contents.split()  
        num_words = len(words)
        print ("The file "+ filename + " has about " + str(num_words)+" words.")
        
filename = input("Please input a filename:")    #输入文件名
count_words(filename)
