# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import json


dict = {"health":{
         "cpu":[0.81,0.66,0.24,0.34,0.15],
         "disk":[0.81,0.66,0.24,0.34,0.15],
         "storage":[0.81,0.66,0.24,0.34,0.15]},
 "devId":1,
 "code_order":1}
test = json.dumps(dict)
train = json.loads(test)
print('数据长度: %d' % len(train['health']))
sample = pd.DataFrame(train['health'])
print(sample)
