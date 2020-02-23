'''
@Author: xiaose
@Date: 2020-02-12 11:02:22
'''

'ReLU函数实现'

import numpy as np
import matplotlib.pylab as plt

def relu(x):
  return np.maximum(0, x)

x = np.arange(-5.0, 5.0, 0.1)
y = relu(x)
plt.plot(x, y)

plt.show()
