
from xgboost import XGBRFRegressor as XGBR
from sklearn.ensemble import RandomForestClassifier as RFC
from sklearn.linear_model import LinearRegression as LR
from sklearn.datasets import load_boston
from sklearn.model_selection import KFold, cross_val_score as CVS, train_test_split
from sklearn.metrics import mean_squared_error as MSE
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime
from time import time
from function import plot_learning_curve

boston = load_boston()
X, y = boston.data, boston.target

x_train, x_test,  y_train, y_test =  train_test_split(X, y, test_size=0.3)

# 构建梯度提升树模型
xgbr = XGBR(n_estimators=100)
xgbr.fit(x_train, y_train)
# 预测结果
predict = xgbr.predict(x_test)


# 计算均方误差
print(MSE(y_test, xgbr.predict(x_test)))

# 绘制学习曲线
cv = KFold(n_splits=5, shuffle=True, random_state=32)
plot_learning_curve(XGBR(n_estimators=100, random_state=30), 'XGBR', X, y, ax=None, cv=cv)
plt.show()

# 通过观察图可以发现在数据量很少的情况下，模型处于过拟合状态，在数据流不断提高时，模型的泛华能力不断提高。


# 开始模型调参，先来绘制n_estimators的学习曲线观察何时最优
axisx = range(100, 300, 10)
rs = []
var = []
ge = []
for i in axisx:
  xgbr = XGBR(n_estimators=i, random_state=30)
  cvresult = CVS(xgbr, X, y, cv=cv)
  # 记录1-偏差
  rs.append(cvresult.mean())
  # 记录方差
  var.append(cvresult.var())
  # 记录泛化误差
  ge.append((1-cvresult.mean())**2 + cvresult.var())
# 打印R2最高的参数取值，并打印此时的方差
print(axisx[rs.index(max(rs))], max(rs), var[rs.index(max(rs))])
# 打印方差最低时对应的参数取值，并打印此时的R2
print(axisx[var.index(min(var))], min(var), rs[var.index(min(var))])
# 打印泛化误差最低时的参数取值
print(axisx[np.argmin(ge)], rs[ge.index(min(ge))], var[ge.index(min(ge))])
plt.plot(axisx, rs, color="r", label="XGBR")
plt.legend()
plt.show()

# 通过观察发现当n_estimators取150时泛华误差最小

# 验证
xgbr = XGBR(n_estimators=100, random_state=420).fit(x_train, y_train)
print(xgbr.score(x_test, y_test))
xgbr = XGBR(n_estimators=150, random_state=420).fit(x_train, y_train)
print(xgbr.score(x_test, y_test))