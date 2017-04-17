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
    
"""存储文件"""
import json

numbers = [1,2,3,4,5,6,6,7]
filename = 'numbers.json'           #指定存储文件的名称，同时生成numbers.json 文件
with open(filename,'w') as f_obj:   #open()使用写入模式
    json.dump(numbers,f_obj)        #json.dump有两个实参，要存储的数据和用于存储数据的文件对象

with open (filename) as f_suj:
    number = json.load(f_suj)
print (number)
