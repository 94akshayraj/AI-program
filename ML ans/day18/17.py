import tensorflow as tf

x = tf.random_normal([2, 3])
y = tf.random_normal([2, 3])
z = tf.random_normal([2, 3])
sum = tf.add(x,5)

sess = tf.Session()
output = sess.run(sum)
print output