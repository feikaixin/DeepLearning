"""
决策树
"""

from sklearn import datasets
from sklearn.tree import DecisionTreeClassifier
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.model_selection import validation_curve
from sklearn.tree import export_graphviz
import graphviz
import matplotlib.pyplot as plt
import numpy as np



wine = datasets.load_wine()
X, Y = wine.data, wine.target

csv = pd.concat([pd.DataFrame(X),  pd.DataFrame(Y)], axis=1)


X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3)

# max_depth 树的深度 
# min_samples_leaf 节点中的样本数必须是多少
# min_samples_split 节点中的样本数满足多少才可以分隔
# min_impurity_decrease 信息增益满足多少才进行分隔
clf = DecisionTreeClassifier(
  criterion="entropy"
  , random_state=30
  , splitter="random"
  , max_depth=4
  , min_samples_leaf=10
  , min_samples_split=10
)
clf.fit(X_train, Y_train)
score = clf.score(X_test, Y_test)

# 可视化不同超参数下训练的优劣
param_range = np.linspace(3, 10, 6, dtype="int")
train_scores, test_scores = validation_curve(
  clf,
  X,
  Y,
  cv=10,
  param_name="max_depth",
  param_range=param_range,
  scoring="accuracy",
)

train_scores_means = np.mean(train_scores, axis=1)
test_scores_means = np.mean(test_scores, axis=1)

plt.plot(param_range, train_scores_means, color="b", label="train_scores_means")
plt.plot(param_range, test_scores_means, color="g", label="test_scores_means")

plt.xlabel("max_depth")
plt.ylabel("accuracy")
plt.legend(loc="best")
plt.show()




# 绘制决策树 通过export_graphviz获取dot节点信息，通过graphviz的Source模块来展示dot信息
feature_name = ["酒精", "苹果酸", "灰", "灰的碱性", "镁", "总酚", "类黄酮", "非黄烷类酚类", "花青素", "颜色强度", "色调", "od280", "铺氨酸"]
dot_data = export_graphviz(
  clf
  , feature_names=feature_name
  , class_names=["琴酒", "雪莉", "贝尔摩德"]
  , rounded=True
  , filled=True
)
graph = graphviz.Source(dot_data)
graph.format = "png"
graph.view()

# 获取哪个特征的重要性  zip把两个list对应，返回一个tuple
importtant = [*zip(feature_name, clf.feature_importances_)]
