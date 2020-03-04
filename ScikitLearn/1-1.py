"基础训练"



import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

# 导入花的数据
iris = datasets.load_iris()

# 花的属性都是在data里面
iris_X = iris.data

# 花的分类在target里面
iris_Y = iris.target

# test_size 表示 测试集占比30%
X_train, X_test, Y_train,  Y_test = train_test_split(iris_X, iris_Y, test_size=0.3)

# 定义K近邻算法模型
knn_model = KNeighborsClassifier()

# 训练数据集
knn_model.fit(X_train, Y_train)

# 开始预测
predict = knn_model.predict(X_test)
print(predict)

print(Y_test)



