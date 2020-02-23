'''
@Author: xiaose
@Date: 2020-02-11 11:51:09
'''
import numpy as np

# 1 引入numpy并查看版本
np.__version__

# 2 创建一位数组，0-9
np.arange(10)

# 创建boolean数组(3x3全部为True)
np.full((3, 3), True)

# 提取满足条件的元素（提取奇数项)
arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
arr1 = arr[ arr % 2 != 0]

# 替换满足条件的元素（替换奇数项为-1）
arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
arr[arr % 2 != 0 ] = -1

# reshape一个数组（0-9这个一维数组->2x5的二维数组）
arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
arr.reshape(2,5)

# 垂直拼接俩数组
a = np.arange(10).reshape(2,-1)
b = np.repeat(1, 10).reshape(2,-1)
np.vstack([a, b])

# 水平拼接俩数组
a = np.arange(10).reshape(2,-1)
b = np.repeat(1, 10).reshape(2,-1)
np.hstack([a, b])

# 求两数组交集
a = np.array([1,2,3,2,3,4,3,4,5,6])
b = np.array([7,2,10,2,7,4,9,4,9,8])
np.intersect1d(a,b)

# 两等长数组，找出位置相同且值也相同的下标
a = np.array([1,2,3,2,3,4,3,4,5,6])
b = np.array([7,2,10,2,7,4,9,4,9,8])
np.where(a == b)

# 计算数组均值、中位数、标准差
a = np.arange(1000)
print(np.mean(a),np.median(a),np.std(a))