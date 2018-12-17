import tensorflow as tf

X = tf.constant([[1,2,3], [4,5,6]])


init = tf.global_variables_initializer()
sess = tf.Session()
sess.run(init)

output = sess.run(X)
print output

sess.close()