'''
@Author: xiaose
@Date: 2020-02-10 10:32:07
'''

# 类
class Man(object):
  def __init__(self, name):
    self.name = name
    print("初始化完成")
    print(self)
  def hello(self):
    print("Hello:" + self.name + "!")

m = Man('xiaose')
m.hello()


# 数据类型
a = 123
b = "str"
c = False
d = None
e = 1.23
f = [1, 2, 3]
g = (1, 2, 3)
h = {"sex": "男", "city": "山西"}

# 条件判断和循环
if 10 > 0:
  print("lala")
elif 20 > 10:
  print("sasa")
else:
  print("endend")


sum = 0
for x in range(101):
    sum = sum + x
print(sum)

sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
print(sum)




