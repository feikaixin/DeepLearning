"用tensorflow加载Fashion minist数据集, 并建立多分类的逻辑回归"

import tensorflow as tf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 加载fashion minist
(train_image, train_label), (test_image, test_label) = tf.keras.datasets.fashion_mnist.load_data()

print(train_image[0])
# 训练集和测试集数字归一化
train_image = train_image/255
test_image = test_image/255

model = tf.keras.Sequential()

# 添加拉伸数组的层
model.add(tf.keras.layers.Flatten(input_shape=(28, 28)))
model.add(tf.keras.layers.Dense(128, activation="relu"))
model.add(tf.keras.layers.Dense(10, activation="softmax"))


# sparse_categorical_crossentropy一般用在连续的数字上
model.compile(
  optimizer="adam",
  loss="sparse_categorical_crossentropy",
  metrics=["acc"]
)
# 这里的优化器也可以用一个optimizers对象，它可以定制化一些参数
# model.compile(
#   optimizer=tf.keras.optimizers.Adam(learning_rate=0.01)
# )

model.fit(train_image, train_label, epochs=5)

# 对模型进行评估
model.evaluate(test_image, test_label)


"""
当label为顺序数字的时候用sparse_categorical_crossentropy
当label为独热编码时使用categorical_crossentropy
"""
# 将数据转换为onehot编码
train_label_onehot = tf.keras.utils.to_categorical(train_label)



