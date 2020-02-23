import random

# 生成0~1之间的随机浮点数
a = random.random()
print(a)

# 生成0~10之间的任意整数
b = random.randint(1, 10)
print(b)

# 在列表中随机选取一个值
c = random.choice([1,2,3,4])
print(c)

# 随机打乱数组
d  = [2,3,1,4,5,6]
random.shuffle(d)
print(d)

