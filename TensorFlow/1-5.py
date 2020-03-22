"""
绘制学习曲线观察模型是否过拟合， 然后添加Dropout层防止过拟合
"""

import tensorflow as tf
from matplotlib import pyplot as plt

(train_image, train_label), (test_image, test_label) = tf.keras.datasets.fashion_mnist.load_data()

# 训练集和测试集数字归一化
train_image = train_image/255
test_image = test_image/255

model = tf.keras.Sequential()

model.add(tf.keras.layers.Flatten(input_shape=(28, 28)))
model.add(tf.keras.layers.Dense(128, activation="relu"))
model.add(tf.keras.layers.Dropout(0.5))
model.add(tf.keras.layers.Dense(128, activation="relu"))
model.add(tf.keras.layers.Dropout(0.5))
model.add(tf.keras.layers.Dense(128, activation="relu"))
model.add(tf.keras.layers.Dropout(0.5))
model.add(tf.keras.layers.Dense(128, activation="relu"))
model.add(tf.keras.layers.Dense(10, activation="softmax"))

model.compile(
  optimizer="adam",
  loss="sparse_categorical_crossentropy",
  metrics=["acc"]
)

history = model.fit(train_image, train_label, epochs=10, validation_data=(test_image, test_label))

plt.plot(history.epoch, history.history.get('loss'), label="loss")
plt.plot(history.epoch, history.history.get('val_loss'), label="validation_loss")
plt.legend()
plt.show()