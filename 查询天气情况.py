# -*- coding: utf-8 -*-
"""
Created on Sun Jun  3 08:48:06 2018

@author: lenovo
"""




print("欢迎使用全球天气app")

import urllib.request as r
city=input("请输入城市：")
address='http://api.openweathermap.org/data/2.5/forecast?q=zhengzhou,cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996&units=metric'
info=r.urlopen(address.format(city)).read().decode('utf-8','ignore')
import json
data=json.loads(info)


for i in range(5):
    b=7*i-6
    a={"时间":data['list'][b]['dt_txt'],
   "天气情况":data['list'][b]['weather'][0]['description'],
   "最高温度":data['list'][b]['main']['temp_max'],
   "最低温度":data['list'][b]['main']['temp_min']}

    print("\n当前时间为："+a["时间"],
      "\n天气状况："+a["天气情况"],
      "\n最高温度为:"+str(a["最高温度"]),
      "\n最低温度为："+str(a["最低温度"]))

      
     
   
      













