import tensorflow as tf
import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv('./dataset/salary.csv')
X = data.Education
Y = data.Income

# 定义一个顺序模型Sequential
model = tf.keras.Sequential()

# 给模型里面添加方法
model.add(tf.keras.layers.Dense(1, input_shape=(1,)))

# 查看模型的整体情况
model.summary()

# 对模型进行训练  optimizer对模型进行优化  loss定义损失函数
model.compile(optimizer="adam", loss="mse")

# 开始训练模型 epochs训练次数
history = model.fit(X, Y, epochs=5000)

# 开始预测
predict = model.predict(pd.Series([20]))

print(predict)