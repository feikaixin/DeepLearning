"""
集成学习 --- 随机森林
"""


from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import validation_curve
from sklearn.model_selection import GridSearchCV
import matplotlib.pyplot as plt
import numpy as np


# 获取红酒数据集
wine = load_wine()
X, Y = wine.data, wine.target

# 将数据划分成训练集和测试集，测试集占30%
x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.3)

# 构建决策树模型 random_state:随机种子，防止每次训练结果不一致
dtc = DecisionTreeClassifier()
# 用训练集数据训练模型
dtc.fit(x_train, y_train)

# 构建随机森林模型
# n_estimators越大越好，不过在达到一定值后效果开始波动，而且还非常占用内存，训练时间也会很长，所以我们需要在内存，训练时间、训练效果中取得平衡点。
rfc = RandomForestClassifier(n_estimators=100)
# 用训练集数据训练模型
rfc.fit(x_train, y_train)


# 绘图观察单个决策树和随机森林的acc
dtc_val=[]
rfc_val=[]
for i in range(10):
  # 用交叉验证法进行打分验证, cv划分几组
  dtc_scores = cross_val_score(dtc, X, Y, scoring="accuracy", cv=10).mean()
  rfc_scores = cross_val_score(rfc, X, Y, scoring="accuracy", cv=10).mean()
  dtc_val.append(dtc_scores)
  rfc_val.append(rfc_scores)

plt.plot(range(1,11), dtc_val, label="Decision Tree", color="red")
plt.plot(range(1,11), rfc_val, label="Random Forest", color="blue")
plt.xlabel("训练次数")
plt.ylabel("交叉沿着精确度")
plt.legend()
plt.show()

# 通过观察图可以发现单个决策树的acc上升，随机森林也随之上升，下降也跟这下降。


# 绘图观察n_estimators的学习曲线
param_range = np.arange(1, 200, dtype="int64")
train_scores, test_scores = validation_curve(
  rfc,
  X,
  Y,
  cv=10,
  param_name="n_estimators",
  param_range=param_range,
  scoring="accuracy"
)
test_scores_means = np.mean(test_scores, axis=1)
print(np.max(test_scores_means), np.argmax(test_scores_means))
plt.plot(param_range, test_scores_means)
plt.title("n_estimators的学习曲线")
plt.xlabel("森林的个数")
plt.ylabel("acc")
plt.show()

# 网格调参
param_grid = {"max_depth": np.arange(1, 20, 1)}
rfc = RandomForestClassifier(n_estimators=39, random_state=30)
GS = GridSearchCV(rfc, param_grid=param_grid, cv=10)
GS.fit(X, Y)
print(GS.best_score_) # 最好的分数是0.9777777
print(GS.best_params_) # 最好的深度是4