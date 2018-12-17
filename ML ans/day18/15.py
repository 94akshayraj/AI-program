import tensorflow as tf

x = tf.random_normal([2, 3])
y = tf.random_normal([2, 3])
diff = tf.subtract(x,y)

sess = tf.Session()
output = sess.run(diff)
print output