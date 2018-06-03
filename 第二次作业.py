# -*- coding: utf-8 -*-
"""
Created on Sat Jun  2 16:50:37 2018

@author: lenovo
"""

import urllib.request as r
city_pinyin=input("请输入城市拼音：")
address='http://api.openweathermap.org/data/2.5/weather?q=meishan&mode=json&units=metric&lang=zh_cn&APPID=6a67ed641c0fda8b69715c43518b6996'
info=r.urlopen(address.format(city_pinyin)).read().decode('utf-8','ignore')
print(info)

import json
data=json.loads(info)

a={"温度":data['main']['temp'],
   "天气情况":data['weather'][0]['description'],
   "最高温度":data['main']['temp_max'],
   "气压":data['main']['pressure']}
print('最高温度为'+str(a["温度"]),
      a["天气情况"],
      a["最高温度"],
      a["气压"])












