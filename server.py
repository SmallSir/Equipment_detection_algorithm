# -*- coding: utf-8 -*-
from flask import Flask
from flask import request
from moder_bulid import model_build
from equiment_pre import IsolationForest
import json
from match_model import match_model
from flask_api import status
from match_model import got_train
app = Flask(__name__)

@app.route('/health',methods=['POST','GET'])
def ac():
    if request.method == 'GET':
        return json.dumps(dict({
            'Error': 'Method Not Allowed',
            'Method': 'Only Accept POST Request'
        })),405
    datas = json.loads(request.get_data().decode())
    devId = datas['devId']
    code_order= datas['code_order']
    data = datas['health']
    k = -1
    for x in data:
        if len(data[x]) != k and k != -1:
            return json.dumps(dict({
                'Error': 'Unsupported Media Type',
                'Input': 'Please Input the Right Dict Type!'
            })),505
        if k == -1:
            k = len(data[x])
    dict_message = {}
    if k != 1:
        model = model_build(data)
        model.model_building()
        return dict({'Outcome': 'The Algorithm Training is Finished Successfully!'}),200
    else:
        dic_message = {}
        iso = IsolationForest(data)
        names = iso.equipment_pred()
        if len(names) != 0:
            '''
            fault_name, fault_sim = match_model(X_test=data)  # 异常名称和异常相似度
            dic_message['fault_name'] = fault_name
            dic_message['fault_same'] = fault_sim
            '''
            dic_message['fault_index_name'] = names
        dic_message['coder_order'] = code_order
        dic_message['devld'] = devId
        return json.dumps(dic_message),200
if __name__ == '__main__':
    app.debug = True
    app.run(host='192.168.0.48',port=8080)



