# -*- coding: utf-8 -*-
"""
Created on Sun Jun  3 08:48:06 2018

@author: lenovo
"""
print("欢迎使用全球天气app")

print("\n是否查看当前城市天气？")
menno=input("请输入菜单：")
if menno=='是':
    print("查看当前城市天气情况")
    import urllib.request as r
    city=input("请输入城市名称：")
    address='http://api.openweathermap.org/data/2.5/forecast?q=zhengzhou,cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996&units=metric'
    info=r.urlopen(address.format(city)).read().decode('utf-8','ignore')
    
    import json
    data=json.loads(info)
    for i in range(1,6):
        d=7*i-6
        a={"时间":data['list'][d]['dt_txt'],
           "天气情况":data['list'][d]['weather'][0]['description'],
           "气压":data['list'][d]['main']['pressure'],
           "最高温度":data['list'][d]['main']['temp_max'],
           "最低温度":data['list'][d]['main']['temp_min']}
        print("\n当前时间为："+a["时间"],
              "\n天气状况："+a["天气情况"],
              "\n气压为："+str(a["气压"]),
              "\n最高温度为:"+str(a["最高温度"]),
              "\n最低温度为："+str(a["最低温度"]))

elif menno=='否':
    print("\n查看其他城市天气情况")
    import urllib.request as r
    city=input("请输入城市名称：")
    address='http://api.openweathermap.org/data/2.5/forecast?q=zhengzhou,cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996&units=metric'
    info=r.urlopen(address.format(city)).read().decode('utf-8','ignore')
    
    import json
    data=json.loads(info)
    for i in range(1,6):
        d=6*i-5
        a={"时间":data['list'][d]['dt_txt'],
           "天气情况":data['list'][d]['weather'][0]['description'],
           "气压":data['list'][d]['main']['pressure'],
           "最高温度":data['list'][d]['main']['temp_max'],
           "最低温度":data['list'][d]['main']['temp_min']}
        print("\n当前时间为："+a["时间"],
              "\n天气状况："+a["天气情况"],
              "\n气压为："+str(a["气压"]),
              "\n最高温度为:"+str(a["最高温度"]),
              "\n最低温度为："+str(a["最低温度"]))    
    
    
     
   
      

















