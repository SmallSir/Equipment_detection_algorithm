# -*- coding: utf-8 -*-
import requests
import json
import demjson
url = 'http://127.0.0.1:5000/health'
dictss = {"health":{
         "cpu":[0.81,0.66,0.24,0.34,0.15],
         "disk":[0.81,0.66,0.24,0.34,0.15],
         "storage":[0.81,0.66,0.24,0.34,0.15]},
 "devId":1,
 "code_order":1}
dicts = {"health":{
         "cpu":[34],
         "disk":[34],
         "storage":[34]},
 "devId":1,

 "code_order":1
}
r= requests.post(url,data = json.dumps(dicts))
print(r.json())