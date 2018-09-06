# coding=utf-8
from Match import Match
from train_data import get_train
import pandas as pd

got_train = False  # 服务器刚启动，没有获取训练集，故为False

def match_model(X_test):
    X_test = pd.DataFrame(X_test)  # 将字典类型转为数据框
    global got_train
    match = Match()
    if not got_train:
        # 服务器刚启动，进入这里执行
        train = get_train()  # 从数据库获取训练集
        got_train = True  # 获取到训练集，改为True
        X_train = train[X_test.colunms]
        print(X_train)
        Y_train = train['异常类别'].values
        print(Y_train)
        match.preprocess(X_train, Y_train, X_test)  # 数据预处理
        return match.prob_fit_pred()[0]
    else:
        # 服务器刚启动不会进入这里运行
        X_train = train[X_test.colunms]
        Y_train = train['异常类别'].values
        match.preprocess(X_train, Y_train, X_test)
        return match.prob_fit_pred()[0]
