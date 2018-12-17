import tensorflow as tf

X = tf.constant([[1, 3, 5], [4, 6, 8]],dtype='float32')


init = tf.global_variables_initializer()
sess = tf.Session()
sess.run(init)

output = sess.run(X)
print output

sess.close()