# coding=utf-8
from Match import Match
import pandas as pd
import pymssql

class Model_control:

    def __init__(self, X_test, code,sys_id=None,devId=None,equipe_type=None):
        self.got_train_1 = False
        self.got_train_2 = False
        self.got_train_3 = False
        self.X_test = pd.DataFrame(X_test)
        self.code = code
        self.sys_id = sys_id
        self.devId = devId
        self.equipe_type = equipe_type

    def match_model(self):
        # 依据code来找对应的数据库
        train = self.get_train()
        X_train = train[self.X_test.columns]
        Y_train = train['异常类别'].values  # 暂定为'异常类别'

        match = Match()
        match.preprocess(X_train, Y_train, X_test)  # 数据预处理

        pred_value, pred_prob = match.prob_fit_pred()
        return pred_value, pred_prob

    def get_train(self):
        # 由于目前数据库未知，故以下代码后期需要更改
        if self.code == '1':  # 暂定为self.code
            if not self.got_train_1:
                conn = pymssql.connect(host='192.168.1.201', user='sa', password='123.com', database='GB_NEW')
                SQL = "select * from [dbo].[GB_APPOINTMENT]"
                self.df_1 = pd.read_sql(SQL, con=conn)
                self.got_train_1 = True  # 表明获取到了code=1的数据
                return self.df_1
            else:  # 否则就表明之前读取过code=1的数据，直接返回就好了
                return self.df_1
            
        elif self.code == '2':
            if not self.got_train_2:
                conn = pymssql.connect(host='192.168.1.201', user='sa', password='123.com', database='GB_NEW')
                SQL = "select * from [dbo].[GB_APPOINTMENT]"
                self.df_2 = pd.read_sql(SQL, con=conn)
                self.got_train_2 = True  # 表明获取到了code=2的数据
                return self.df_2
            else:
                return self.df_2

        else:
            if not self.got_train_3:
                conn = pymssql.connect(host='192.168.1.201', user='sa', password='123.com', database='GB_NEW')
                SQL = "select * from [dbo].[GB_APPOINTMENT]"
                self.df_3 = pd.read_sql(SQL, con=conn)
                self.got_train_3 = True  # 表明获取到了code=3的数据
                return self.df_3
            else:
                return self.df_3