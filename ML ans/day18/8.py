import tensorflow as tf


zero = tf.linspace(5.0,10.0,50)


sess = tf.Session()
output = sess.run(zero)
print output