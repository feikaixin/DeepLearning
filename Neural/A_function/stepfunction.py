'''
@Author: xiaose
@Date: 2020-02-11 19:24:29
'''


'阶跃函数的实现'

import numpy as np
import matplotlib.pylab as plt
def step_function(x):
  return np.array(x > 0, dtype=np.int)

x = np.arange(-5.0, 5.0, 0.1)
y = step_function(x)
plt.plot(x, y)
plt.ylim(-0.1, 1.1)
plt.show()