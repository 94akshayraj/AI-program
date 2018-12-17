import tensorflow as tf

zero = tf.random_uniform([3, 2], 0,2)


sess = tf.Session()
output = sess.run(zero)
print output