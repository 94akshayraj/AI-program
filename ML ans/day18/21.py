import tensorflow as tf

w = tf.Variable(1.0,name="weight")
h = tf.Variable(2.0,name="height")
b = tf.Variable(3.0,name="breadth")
sum = tf.add(w,(tf.add(h,b)))

init = tf.global_variables_initializer()
sess = tf.Session()
sess.run(init)
output = sess.run(sum)
print output