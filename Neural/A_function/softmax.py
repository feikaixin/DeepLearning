'''
@Author: xiaose
@Date: 2020-02-12 12:42:53
'''


'softmax函数实现'

import numpy as np

def softmax(a):
  # 此刻的c是为了防止指数过大导致溢出
  c = np.max(a)
  exp_a = np.exp(a - c)
  sum_exp_a = np.exp(exp_a)
  y = exp_a / sum_exp_a

  return y

