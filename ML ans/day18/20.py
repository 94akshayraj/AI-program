import tensorflow as tf

w = tf.Variable(1.0,name="weight")

init = tf.global_variables_initializer()
sess = tf.Session()
sess.run(init)
output = sess.run(w)
print output