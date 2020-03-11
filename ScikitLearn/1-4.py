"""
数据normalization, preprocessing模块
"""

from sklearn import preprocessing
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.datasets import make_classification
from sklearn.svm import SVC
import matplotlib.pyplot as plt
# a = np.array([[10, 2.7, 3.6], [-100, 5, -2], [120, 20, 40]], dtype=np.float64)

# print(a)
# print(preprocessing.scale(a))

X, Y = make_classification(
  n_samples=300, 
  n_features=2, 
  n_redundant=0, 
  n_informative=2, 
  random_state=22, 
  n_clusters_per_class=1, 
  scale=100)


X = preprocessing.minmax_scale(X, feature_range=(-1, 1))

train_X, test_X, train_Y, test_Y = train_test_split(X, Y, test_size=0.3)

clf = SVC()
clf.fit(train_X, train_Y)

# 这里的score返回的是R^2指标
print(clf.score(test_X, test_Y))