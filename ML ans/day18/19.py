import tensorflow as tf

x = tf.random_normal([2, 3])
y = tf.random_normal([2, 3])
z = tf.random_normal([2, 3])
sum = tf.add(x,(tf.add(y,z)))

sess = tf.Session()
writer = tf.summary.FileWriter('./tb18',sess.graph)

sess = tf.Session()
output = sess.run(sum)
print output