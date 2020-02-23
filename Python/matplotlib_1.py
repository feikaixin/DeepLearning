'''
@Author: xiaose
@Date: 2020-02-11 12:00:30
'''

import matplotlib.pyplot as plt
import numpy as np

# 以0.1为单位，生成0到6的数据
x = np.arange(0, 6, 0.1)
y1 = np.sin(x)
y2 = np.cos(x)
# 图标的形状 -- 默认
plt.plot(x, y1, linestyle="-", label="sin")
plt.plot(x, y2, linestyle="--", label="cos")
# 图标的形状 -- 柱状图
plt.bar(x, y1)
# 图标的形状 -- 
# 图标的横坐标
plt.xlabel("x")
# 图标的纵坐标
plt.ylabel("y")
# 图标的标题
plt.title("sin & cos")
# 图的大小
plt.figure(figsize=(10, 10))
# 图表显示图例
plt.legend()
plt.show()