"""
贝叶斯算法示例: 高斯朴素贝叶斯
"""

import numpy as np
from sklearn import datasets
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt


digits = datasets.load_digits()
X, Y = digits.data, digits.target

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=666)

# 实例化 建模
gnb = GaussianNB().fit(X_train, Y_train)

# 查看分数
gnb.score(X_test, Y_test)

Y_pred = gnb.predict(X_test)

# 这里Y_pred 是对所有样本的概率估计 并且最后去的概率最大的值
Y_pred.shape

Y_pred[1, :].sum()

