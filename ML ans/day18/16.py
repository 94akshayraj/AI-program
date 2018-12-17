import tensorflow as tf

x = tf.random_normal([2, 3])
y = tf.random_normal([2, 3])
prod = tf.multiply(x,y)

sess = tf.Session()
output = sess.run(prod)
print output