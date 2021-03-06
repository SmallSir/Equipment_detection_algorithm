# -*- coding: utf-8 -*-
from flask import Flask
from flask import request
from moder_bulid import model_build
import json
from flask_api import status
app = Flask(__name__)


@app.route('/train',methods=['POST','GET'])
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
        if len(data[x]) != k and k != -1:  # 特征值的数据数量不同解决办法
            return json.dumps(dict({
                'Error': 'Unsupported Media Type',
                'Input': 'Please Input the Right Dict Type!'
            })), 505
        if k == -1:
            k = len(data[x])
    # 建模操作
    model = model_build(train = data,code = code_order,sys_id = sys_id,equip_type = equip_type,dev_ids = dev_ids)
    model.model_building()
    return json.dumps(dict({'Outcome': 'The Algorithm Training is Finished Successfully!'})), 200

if __name__ == '__main__':
    app.debug = True
    app.run()