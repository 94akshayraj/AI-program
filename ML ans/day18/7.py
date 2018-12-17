import tensorflow as tf


zero = tf.fill([2, 3], 4)


sess = tf.Session()
output = sess.run(zero)
print output