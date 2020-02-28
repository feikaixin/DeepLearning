"线性回归"
import tensorflow as tf
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('./dataset/Advertising.csv')

# 选取特征值
x = data.iloc[:, 1:-1]
y = data.iloc[:, -1]
 
# 建立顺序模型
model = tf.keras.Sequential([
  tf.keras.layers.Dense(10, input_shape=(3,), activation="relu"),
  tf.keras.layers.Dense(1)
])

# 查看模型的整体情况
model.summary()

# 对模型进行编译
model.compile(optimizer="adam", loss="mse")

# 开始训练
model.fit(x, y, epochs=100)

# 开始预测
test = data.iloc[:10, 1:-1]
print(test)
predict = model.predict(test)

# print(predict)
