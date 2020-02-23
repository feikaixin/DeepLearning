'''
@Author: xiaose
@Date: 2020-02-11 20:51:06
'''


'sigmoid函数实现'

import numpy as np

def sigmoid(x):
  return 1 / (1 + np.exp(-x))