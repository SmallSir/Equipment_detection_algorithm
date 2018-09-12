# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.externals import joblib

class model_build():
    def __init__(self,train,**kwargs):
        self.train = pd.DataFrame(train)
        self.code = kwargs['code']  # 业务代码
        self.equip_type = kwargs['equip_type']# 设备类型
        self.sys_id = kwargs['sys_id']  # 系统id号码
        self.dev_ids = kwargs['dev_ids']  # 设备id
    def model_building(self):#对整体进行孤异森林模型构建和各个特征值孤异森林模型构建
        isolations = IsolationForest(bootstrap=False,contamination=0.02)
        isolations.fit(self.train)
        joblib.dump(isolations,"业务代码" + self.code+"设备类型"+self.equip_type+"系统id" + self.sys_id+"设备id"+self.dev_ids+ 'equipment.m')
        for x in range(self.train.shape[1]):#各个特征值孤异森林模型构建
            isolation = IsolationForest(bootstrap=False,contamination=0.02)
            isolation.fit(np.array(self.train.iloc[:,x]).reshape(-1,1))
            joblib.dump(isolation,filename="业务代码" + self.code+"设备类型"+self.equip_type+"系统id" + self.sys_id+"设备id"+self.dev_ids+ self.train.columns[x]+".m")

