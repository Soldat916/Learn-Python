# -*- coding: utf-8 -*-
"""
Created on Tue Mar 2017
@author: jiang
"""
#列表间元素的移动
unconfirmed_users  = ['alice','brain','candace']
confirmed_users = []
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print ("verifyling user:"+  current_user.title())
    confirmed_users.append(current_user)

print ("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print (confirmed_user.title())

#字典的填充
responses = {}
#设置一个标志
active = True
while active:
    #提示被调查的名字和回答
    name = input("\nWhat's your name? ")
    response = input("Which mountain would you like to climb someday? ")
    #将答案存储在字典中
    responses[name] = response

    repeat =  input("Would you like to let another person respond? (Yes/ No)")
    if repeat == 'no':
        active = False
print ("\n---Poll results ---")
for name, response in responses.items():
    print (name + "would like to climb" + response + ".")

#While语句的基本使用
prompt = "\nTell me something,and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

active = True   #设置一个标志
while active:
    message  = input(prompt)

    if message == 'quit':          
        active = False             #break
    else:
        print(message)


