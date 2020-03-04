"""
model常用的属性和功能
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

# 获取模型的参数 intercept_相当于ax+b中的b
print(model.coef_)
print(model.intercept_)

# 对模型进行打分
model.score(data_X, data_Y)

# 获取模型参数
model.get_params()

# 模型预测
print(model.predict(data_X[:4]))
print(data_Y[:4])