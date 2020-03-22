"""
tf.keras 的函数式API
"""

from tensorflow import keras


(train_image, train_label), (test_image, test_label) = keras.datasets.fashion_mnist.load_data()

# 训练集和测试集数字归一化
train_image = train_image/255
test_image = test_image/255

inputs = keras.Input(shape=(28, 28))
x = keras.layers.Flatten()(inputs)
x = keras.layers.Dense(128, activation="relu")(x)
x = keras.layers.Dropout(0.5)(x)
x = keras.layers.Dense(128, activation="relu")(x)
outputs = keras.layers.Dense(10, activation="softmax")(x)

model = keras.Model(inputs=inputs, outputs=outputs)

model.summary()