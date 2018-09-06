# -*- coding: utf-8 -*-
from flask import Flask
from flask import request
from moder_bulid import model_build
from equiment_pre import IsolationForest
import json
#from match_model import match_model
from flask_api import status
app = Flask(__name__)

@app.route('/',methods=['POST'])
def ac():
    datas = json.loads(request.get_data().decode())
    devId = datas['devId']
    code_order= datas['code_order']
    data = datas['health']
    k = -1
    for x in data:
        if len(data[x]) != k and k != -1:
            return json.dumps(status.HTTP_505_HTTP_VERSION_NOT_SUPPORTED)
        if k == -1:
            k = len(data[x])
    dict_message = {}
    if k != 1:
        model = model_build(data)
        model.model_building()
        return json.dumps(200)
    else:
        dic_message = {}
        iso = IsolationForest(data)
        names = iso.equipment_pred()
        if len(names) != 0:
            got_train = False
            ''''
            fault_name, fault_sim = match_model(X_test=data,got_train)  # 异常名称和异常相似度
            dic_message['异常名称'] = fault_name
            dic_message['异常相似度'] = fault_sim
            '''
            dic_message['异常指标名称'] = names
            dic_message['coder_order'] = code_order
            dic_message['devld'] = devId
        return json.dumps(dic_message)
if __name__ == '__main__':
    app.debug = True
    app.run(host = '192.168.0.36',port = 8080)



