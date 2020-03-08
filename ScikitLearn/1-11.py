"""
对非线性的数据 采用多项式特征或核函数
多项式：PolynomialFeatures
"""

from sklearn import datasets
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures, StandardScaler
from sklearn.svm import LinearSVC
from sklearn.pipeline import Pipeline
from function import plot_decision_boundary


X, Y = datasets.make_moons(noise=0.15, random_state=666)


# 定义多项式数据函数
def PolynomialSVC(degree, C=1.0):
  return Pipeline([
    ("poly", PolynomialFeatures(degree=degree)),
    ("std_scaler", StandardScaler()),
    ("linearSVC", LinearSVC(C=C)) 
  ])

poly_svc = PolynomialSVC(3)
poly_svc.fit(X, Y)
plot_decision_boundary(poly_svc, axis=[-1.5, 2.5, -1.0, 2.0])
plt.scatter(X[Y==0, 0], X[Y==0, 1])
plt.scatter(X[Y==1, 0], X[Y==1, 1])
plt.show()
