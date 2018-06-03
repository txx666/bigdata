# -*- coding: utf-8 -*-
"""
Created on Sat Jun  2 14:34:35 2018

@author: lenovo
"""

s=['星期一','星期二','星期三','星期四','星期五','星期六','星期天']
for i in s:
    if i == '星期六':
        print('今天是:'+i)
    else:
        print(i)



s=['星期一',
   '星期二',
   '星期三',
   '星期四',
   '星期五',
   '星期六',
   '星期天']
print(s[0])
print(s[1])
print(s[2])
print(s[3])
print(s[4])
print('jintianshi:'+s[5].format(s[5]))
print(s[6])