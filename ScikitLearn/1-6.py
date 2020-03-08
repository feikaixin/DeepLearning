"""
交叉验证 learning_curve:展示不同的数据量，算法的学习得分
"""

from sklearn.model_selection import learning_curve
import matplotlib.pyplot as plt
from sklearn.datasets import load_digits
from sklearn.svm import SVC
import numpy as np

data = load_digits()

X = data.data
Y = data.target

print(X.shape)

train_sizes, train_scores, test_scores = learning_curve(
  SVC(gamma=0.001),
  X,
  Y,
  cv=10,
  scoring="neg_mean_squared_error",
  train_sizes=[0.1, 0.25, 0.5, 0.75, 1],
)

# axis表示对每一行求均值
train_scores_means = -np.mean(train_scores, axis=1)
test_scores_means = -np.mean(test_scores, axis=1)

plt.plot(train_sizes, train_scores_means, color="b", label="trainning")
plt.plot(train_sizes, test_scores_means, color="g", label="cross-validation")

plt.xlabel("Traning samples")
plt.ylabel("loss")
plt.legend(loc="best")
plt.show()