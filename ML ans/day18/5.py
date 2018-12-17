import tensorflow as tf

zero = tf.fill([2, 3], 5)


sess = tf.Session()
output = sess.run(zero)
print output