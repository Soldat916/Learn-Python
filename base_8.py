# -*- coding: utf-8 -*-
"""
Created on Mon April 2017
@author: jiang
"""
"""读取文件"""
file_path = 'D:\Documents\Python\pi_digits.txt'
with open(file_path) as file_object:

    lines  = file_object.readlines()
pi_lines =  ''
for line in lines:
    pi_lines += line.rstrip()
print(pi_lines)

name =input("Enter your birthday,in the form mmddyy: ")
if name in pi_lines:
    print ("Your birthday appears in the digit in pi!")
else:
    print ("Your birthday doesn't appear in the digit in pi!") 

"""写入文件"""
write_path = 'D:\Documents\Python\ex1.txt'

with open(write_path,'w') as write_object:
    write_object.write("I love you!\n")
    write_object.write(input("Please input a msg!")+"\n")     #插入换行符\n.

"""附加文件"""
with open(write_path,'a') as write_ob:
    write_ob.write("This is a test documents!\n")
