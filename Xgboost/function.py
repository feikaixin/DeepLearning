from sklearn.model_selection import learning_curve
import numpy as np
from matplotlib.colors import ListedColormap
import matplotlib.pyplot as plt

def plot_learning_curve(model, title, x, y, ax=None, ylim=None, cv=None, n_jobs=None):
  train_sizes, train_scores, test_scores = learning_curve(
    model, x, y
    , cv=cv
    , shuffle=True
    , n_jobs=n_jobs)
  print(train_scores.shape)
  if ax == None:
    ax = plt.gca()
  else:
    ax = plt.figure()
  
  ax.set_title(title)
  if ylim is not None:
    ax.set_ylim(*ylim)
  ax.set_xlabel("Traning examples")
  ax.set_ylabel("Scores")
  ax.grid() # 绘制网格
  ax.plot(train_sizes, np.mean(train_scores, axis=1), "o-", color="r", label="Traning Score")
  ax.plot(train_sizes, np.mean(test_scores, axis=1), "o-", color="b", label="Test Score")
  # loc表示设置图例位置
  ax.legend(loc="best")
  return ax

