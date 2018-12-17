import tensorflow as tf

zero_t = tf.zeros([2,3])

sess = tf.Session()
output = sess.run(zero_t)
print output