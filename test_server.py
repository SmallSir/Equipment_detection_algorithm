# -*- coding: utf-8 -*-
import requests
import json
url = 'http://192.168.0.36:8080/'
dict = {"health":{
         "cpu":[0.81,0.66,0.24,0.34,0.15],
         "disk":[0.81,0.66,0.24,0.34,0.15],
         "storage":[0.81,0.66,0.24,0.34,0.15]},
 "devId":1,
 "code_order":1}
dict = {"health":{
         "cpu":[81],
         "disk":[81],
         "storage":[81]},
 "devId":1,
 "code_order":1
}
test = json.dumps(dict)
r= requests.post(url,data = json.dumps(dict))
print(r.json())
print(r)