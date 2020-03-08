"""
用LinearSVC 模拟生成二分类问题
"""

from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
from sklearn.svm import LinearSVC
from sklearn import datasets
from function import plot_decision_boundary



data = datasets.load_iris()

X = data.data
Y = data.target

X = X[Y<2, :2]
Y = Y[Y<2]

# 格式化数据
scaler = StandardScaler()
scaler.fit(X)
X_standard = scaler.transform(X)

# 初始化模型 C的值越大代表的是硬间隔  C值越小代表的是软件隔
svc = LinearSVC(C=1e9)
svc.fit(X_standard, Y)



plot_decision_boundary(svc, axis=[-3,3,-3,3])
plt.scatter(X_standard[Y==0, 0], X_standard[Y==0, 1])
plt.scatter(X_standard[Y==1, 0], X_standard[Y==1, 1])
plt.show()