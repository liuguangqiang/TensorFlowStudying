import tensorflow as tf

hello = tf.constant("Hello World!")
sess = tf.compat.v1.Session()
print sess.run(hello)