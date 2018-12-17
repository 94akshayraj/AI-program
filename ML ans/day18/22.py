import tensorflow as tf

w = tf.placeholder(tf.float32)

init = tf.global_variables_initializer()
sess = tf.Session()
sess.run(init)
output = sess.run(w,{w:1.0})
print output