# -*- coding: utf-8 -*-
"""
Created on Mon Mar 2017
@author: jiang
"""
favorite_language = {           # 定位字典
    'jens':['python','ruby'],
    'sarsh':['c'],
    'edword':['ruby','go'],
    'phill':['python','java'],
}
for name, languages in favorite_language.items():  #遍历字典的键值
    if len(languages) == 1:
        print ("\n"+ name.title()+ " 's favorite language is:"+ str(languages[0].title()))
    else:
        print ("\n"+ name.title() + "'s favorite language are:")
        for language in languages:
            print ("\t"+ language.title())
