"""
tf.data模块
"""
# import tensorflow as tf

# dataset = tf.data.Dataset.from_tensor_slices([1, 2, 3])

# dataset = dataset.map(tf.square)



# # 取前几个值
# dataset = dataset.take(5)

# # 乱序
# dataset = dataset.shuffle(7)

# # batch
# dataset = dataset.batch(3)

import tensorflow as tf
import numpy as np 
from sklearn import datasets 
iris = datasets.load_iris()


# ds1 = tf.data.Dataset.from_tensor_slices((iris["data"],iris["target"]))
# for features,label in ds1.take(5):
#     print(features.numpy())
#     print(label.numpy())


ds1 = tf.data.Dataset.from_tensor_slices([[1,2,3], [3, 4, 5]])
ds2 = tf.data.Dataset.from_tensor_slices([1, 2])
ds_zip = tf.data.Dataset.from_tensor_slices((ds1,ds2))
for x,y in ds_zip:
    print(x.numpy(),y.numpy())