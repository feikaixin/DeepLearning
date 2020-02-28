"单分类的逻辑回归"
import tensorflow as tf
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('./dataset/credit-a.csv', header=None)

# 获取数据
x = data.iloc[:, 0:-1]
# 用replace方法替换-1
y = data.iloc[:, -1].replace(-1, 0)

# 定义模型
model = tf.keras.Sequential()

# 给模型里面添加层
model.add(tf.keras.layers.Dense(4, input_shape=(15,), activation="relu"))
model.add(tf.keras.layers.Dense(4, activation="relu"))
model.add(tf.keras.layers.Dense(1, activation="sigmoid"))

# 查看模型总体情况
# model.summary()

# 对模型进行编译 metrics=["acc"]表示输出正确率
model.compile(
  optimizer="adam",
  loss="binary_crossentropy",
  metrics=["acc"]
)

# 这里的histroy 是一个dict里面存放了一些信息
history = model.fit(x, y, epochs=100)

# print(history.history.keys())


# 通过plt进行绘图
plt.plot(history.epoch, history.history.get('loss'))
plt.show()

