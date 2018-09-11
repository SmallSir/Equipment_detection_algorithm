# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.externals import joblib
class IsolationForest():
    def __init__(self,test,code): #train为以往数据路径，test为获取的即时数据
        self.test = pd.DataFrame(test)
        self.code = code
    def equipment_pred(self):#对一组数据进行整体的预测，同时对于异常数据进行各个特征值预测
        isolation = joblib.load(self.code + "equipment.m")
        pred_ = isolation.predict(self.test)        	
        unusual_data = [] #异常数据存放
        if pred_ == -1:
            for x in range(self.test.shape[1]):
                data_pred_,name = self.data_pred(x)
                if not data_pred_:
                    unusual_data.append(name)
        return unusual_data
    def data_pred(self,x):#对各个特征值进行预测
        isolation = joblib.load(self.code + self.test.columns[x]+".m")
        pred_ = isolation.predict(np.array(self.test.iloc[:,x]).reshape(-1,1))
        if pred_ == 1:
            return True,self.test.columns[x]
        else:
            return False,self.test.columns[x]
        
            
