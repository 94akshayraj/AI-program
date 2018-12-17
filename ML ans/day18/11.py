import tensorflow as tf


X = tf.constant([[1, 2], [3, 4], [5, 6]])
swap = tf.random_shuffle(X)

sess = tf.Session()
output = sess.run(swap)
print output