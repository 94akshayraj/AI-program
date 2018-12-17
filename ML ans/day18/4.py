import tensorflow as tf

X = tf.constant([[1,2,3],[4,5,6]])
y = tf.ones_like(X)

init = tf.global_variables_initializer()
sess = tf.Session()
sess.run(init)

output = sess.run(y)
print output

sess.close()