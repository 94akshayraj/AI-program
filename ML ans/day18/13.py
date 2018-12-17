import tensorflow as tf

X = tf.constant([[-1, -2, -3], [0, 1, 2]])
y = tf.zeros_like(X)

out = tf.not_equal(X, y)

init = tf.global_variables_initializer()
sess = tf.Session()
sess.run(init)

output = sess.run(out)
print output

sess.close()