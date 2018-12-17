import tensorflow as tf

X = tf.random_normal([10,10,3])

zero = tf.random_crop(X, [5,5,3])

sess = tf.Session()
output = sess.run(zero)
print output