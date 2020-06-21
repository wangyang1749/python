import tensorflow as tf
import numpy as np

# create data
x_data = np.random.rand(100).astype(np.float32)
y_data = x_data*0.1 + 0.3

# create tensorflow structure
Weights = tf.Variable(tf.random.uniform((1,), -1.0, 1.0))
biases = tf.Variable(tf.zeros((1,)))

loss = lambda: tf.keras.losses.MSE(y_data, Weights * x_data + biases)  # alias: tf.losses.mse
optimizer = tf.keras.optimizers.SGD(learning_rate=0.5)  # alias: tf.optimizers.SGD

for step in range(201):
    optimizer.minimize(loss, var_list=[Weights, biases])
    if step % 20 == 0:
        print("{} step, weights = {}, biases = {}".format(step, Weights.read_value(), biases.read_value()))  # read_value函数可用numpy替换