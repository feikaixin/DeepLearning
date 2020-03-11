'''
@Author: xiaose
@Date: 2020-02-11 12:00:30
'''

# pyplot有当前的图形（figure）和当前的轴（axes）的概念，
# 所有的作图命令都是对当前的对象作用。可以通过gca()获得当前的axes（轴），
# 通过gcf()获得当前的图形（figure）

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

# 创建第一个画板（figure）
plt.figure(1) 
# 第一个画板的第一个子图，表示将这个画板分隔成两行一列，当前处在第一列
plt.subplot(211) 
plt.plot([1, 2, 3])
plt.subplot(212) # 第一个画板的第二个子图
plt.plot([4, 5, 6])
plt.figure(2) #创建第二个画板
plt.plot([4, 5, 6]) # 默认子图命令是subplot(111)
plt.figure(1) # 调取画板1; subplot(212)仍然被调用中
plt.subplot(211) #调用subplot(211)
# xticks表示设置刻度
plt.xticks([1,2,3])
plt.yticks([1,2,3], ['$nomal\ bad$', '$lala$', '$yuyu$'])
plt.title('Easy as 1, 2, 3') # 做出211的标题

# 通过gca获取当前坐标轴
ax = plt.gca()
ax.set_title('fei')
# 使用spines设置边框 设置坐标轴颜色
ax.spines['bottom'].set_color('blue')



plt.show()