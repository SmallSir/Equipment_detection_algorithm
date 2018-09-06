# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.externals import joblib

class model_build():
    def __init__(self,train):
        self.train = pd.DataFrame(train)
    def model_building(self):#对整体进行孤异森林模型构建和各个特征值孤异森林模型构建
        isolations = IsolationForest(bootstrap=False,contamination=0.02)
        isolations.fit(self.train)
        joblib.dump(isolations,'equipment.m')
        for x in range(self.train.shape[1]):#各个特征值孤异森林模型构建
            isolation = IsolationForest(bootstrap=False,contamination=0.02)
            isolation.fit(np.array(self.train.iloc[:,x]).reshape(-1,1))
            joblib.dump(isolation,filename=self.train.columns[x]+'.m')

