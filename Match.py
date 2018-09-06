import numpy as np
import pandas as pd

class Match:
    
    def __init__(self):
        pass
    
    def preprocess(self, X_train, Y_train, X_test):
        
        """功能：对训练数据和测试数据进行预处理（标准化）"""
        
        self.Y_train = Y_train

        from pandas import Series, DataFrame        
        from sklearn import preprocessing
        
        """对训练集进行标准化"""
        scaler = preprocessing.StandardScaler().fit(X_train)
        self.X_train_scaled = DataFrame(scaler.transform(X_train))  # 默认按feature标准化
        
        """对测试集进行标准化"""
        self.X_test_scaled = DataFrame(scaler.transform(X_test))
    
    def nearst_fit_pred(self):
        
        """功能：对训练数据进行拟合，并且对测试数据进行预测"""
        """本函数：使用非参数方法，用最近邻点的类估计（离测试点最近的点的类作为该测试点的类）"""
        from sklearn import neighbors
        clf = neighbors.KNeighborsClassifier(n_neighbors=1)
        clf.fit(self.X_train_scaled, self.Y_train)
        return clf.predict(self.X_test_scaled)
    
    def topn_fit_pred(self, n):
        
        """功能：对训练数据进行拟合，并且对测试数据进行预测"""
        """本函数：使用非参数方法，用距离测试点最近的n个样本估计（根据这n个点进行投票，然后直接进行分类）"""
        from sklearn import neighbors
        clf_K = neighbors.KNeighborsClassifier(n_neighbors=n)
        clf_K.fit(self.X_train_scaled, self.Y_train)
        Y_pred = clf_K.predict(self.X_test_scaled)
        dist, index = clf_K.kneighbors(self.X_test_scaled)
        return self.which_class(index, 5)   
        """输出：每一行代表这个测试点最有可能的n个类别"""
    
    def which_class(self, index, show_n=3):
        from numpy import array
        classes = []
        if show_n > 1:  # 选取前show_n个最可能的类别
            for index_i in index:
                classes.append(list(self.Y_train[index_i].value_counts()[:show_n].index))
            classes = array(classes)
        else:  # 选取最可能的那个类别
            for index_i in index:
                classes.append(self.Y_train[index_i].value_counts().idxmax())
            classes = array(classes)
        return classes
    
    
    def prob_fit_pred(self):
        
        """功能：对训练数据进行拟合，并且对测试数据进行预测"""
        """本函数：依据概率进行分类（朴素贝叶斯）,根据概率对测试点进行分类（将该点分给最可能的那个类别）"""
        from sklearn.naive_bayes import GaussianNB
        clf = GaussianNB()
        clf.fit(self.X_train_scaled, self.Y_train)
        pred_value = clf.predict(self.X_test_scaled)[0]
        pred_prob = clf.predict_prob(self.X_test_scaled)[pred_value]
        return pred_value, pred_prob