import tensorflow as tf

x = tf.random_normal([2, 3])
y = tf.random_normal([2, 3])
sum = tf.add(x,y)

sess = tf.Session()
output = sess.run(sum)
print output