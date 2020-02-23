'交叉熵误差'

import numpy as np

def cross_entropy_error(y, t):
  # 表示10的负7次方
  delta = 1e-7
  return -np.sum(t * np.log(y + delta))
