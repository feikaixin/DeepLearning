"""
交叉验证： validation_curve:展示某个超参数的不同取值的算法总得分
"""

from sklearn.model_selection import validation_curve
import matplotlib.pyplot as plt
from sklearn.datasets import load_digits
from sklearn.svm import SVC
import numpy as np

data = load_digits()

X = data.data
Y = data.target

param_range = np.logspace(-6, -2.3, 5)
train_scores, test_scores = validation_curve(
  SVC(),
  X,
  Y,
  cv=10,
  param_name="gamma",
  param_range=param_range,
  scoring="neg_mean_squared_error"
)

# axis表示对每一行求均值
train_scores_means = -np.mean(train_scores, axis=1)
test_scores_means = -np.mean(test_scores, axis=1)

plt.plot(param_range, train_scores_means, color="b", label="gamma")
plt.plot(param_range, test_scores_means, color="g", label="cross-validation")

plt.xlabel("gamma")
plt.ylabel("loss")
plt.legend(loc="best")
plt.show()