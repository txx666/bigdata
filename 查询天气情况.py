# -*- coding: utf-8 -*-
"""
Created on Sun Jun  3 08:48:06 2018

@author: lenovo
"""

import urllib.request as r
url='http://api.openweathermap.org/data/2.5/weather?q=beijing&mode=xml&units=metric&lang=zh_cn&APPID=6aca3ba66b44ae7c4c78b3cedd7dc84e'
info=r.urlopen(url.format('leshan')).read().decode('utf-8','ingnore')
import json
w=json.loads(info)

















