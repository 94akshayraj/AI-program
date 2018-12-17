import tensorflow as tf

w = tf.placeholder(tf.float32)
h = tf.placeholder(tf.float32)
b = tf.placeholder(tf.float32)
sum = tf.add(w,(tf.add(h,b)))

init = tf.global_variables_initializer()
sess = tf.Session()
sess.run(init)
output = sess.run(sum,{w:1.0,h:2.0,b:3.0})
print output