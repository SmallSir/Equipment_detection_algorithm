# -*- coding: utf-8 -*-
import requests
import json
url = 'http://192.168.0.48:8080/health'
dict = {"health":{
         "cpu":[0.81,0.66,0.24,0.34,0.15],
         "disk":[0.81,0.66,0.24,0.34,0.15],
         "storage":[0.81,0.66,0.24,0.34,0.15]},
 "devId":1,
 "code_order":1}
dict = {"health":{
         "cpu":[34,11],
         "disk":[34],
         "storage":[34]},
 "devId":1,

 "code_order":1
}
test = json.dumps(dict)
r= requests.get(url,data = json.dumps(dict))

print(r.json())