"""
了解scikitlearn中的datasets
1、scikitlearn中有一些现存的数据集
2、scikitlearn中也可以自己创造一些数据集
"""

from sklearn import datasets
from sklearn.linear_model import LinearRegression

# 加载波士顿房价
data = datasets.load_boston()

# 特征值都是在data属性上, 结果都是在target上
data_X = data.data
data_Y = data.target

# 定义模型
model = LinearRegression()
model.fit(data_X, data_Y)


# 模拟创造线性回归的数据
X, Y = datasets.make_regression(n_samples=100, n_features=1, n_targets=1, noise=1)