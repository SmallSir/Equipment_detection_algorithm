# -*- coding: utf-8 -*-
from flask import Flask
from flask import request
from moder_bulid import model_build
from equiment_pre import IsolationForest
import json
from flask_api import status
from match_model import Model_control
app = Flask(__name__)

@app.route('/health',methods=['POST','GET'])
def ac():
    if request.method == 'GET':    #请求方式错误解决方法
        return json.dumps(dict({
            'Error': 'Method Not Allowed',
            'Method': 'Only Accept POST Request'
        })),405
    datas = json.loads(request.get_data().decode())
    #将接收数据赋给变量
    sys_id = str(datas['sys_id'])
    equip_type = str(datas['equip_type'])
    dev_ids = str(datas['devId'])
    code_order = str(datas['code_order'])
    data = datas['health']
    #检测接收的数据是否存在每个特征值的数据数量不同的情况
    k = -1
    for x in data:
        if len(data[x]) != k and k != -1: #特征值的数据数量不同解决办法
            return json.dumps(dict({
                'Error': 'Unsupported Media Type',
                'Input': 'Please Input the Right Dict Type!'
            })),505
        if k == -1:
            k = len(data[x])
    dict_message = {}
    #异常值检测
    dic_message = {}
    iso = IsolationForest(test  = data,code = code_order,sys_id = sys_id,dev_ids =  dev_ids,equip_type = equip_type)
    names = iso.equipment_pred()
    #数据为异常值
    if len(names) != 0:
        model_control = Model_control(X_test=data,code = code_order,sys_id = sys_id,dev_ids = dev_ids,equip_type = equip_type)  # 异常名称和异常相似度
        fault_name, fault_sim = model_control.match_model()  # 对异常数据进行匹配，返回异常名称和异常相似度
        dic_message['fault_name'] = fault_name
        dic_message['fault_same'] = fault_sim
    dic_message['fault_index_name'] = names
    dic_message['coder_order'] = code_order
    dic_message['devld'] = dev_ids
    dic_message['equip_type'] = equip_type
    dic_message['sys_id'] = sys_id
    return json.dumps(dic_message),200
if __name__ == '__main__':
    app.debug = True
    app.run()



