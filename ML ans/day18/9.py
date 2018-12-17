import tensorflow as tf

zero = tf.random_normal([3,2], stddev=2)


sess = tf.Session()
output = sess.run(zero)
print output