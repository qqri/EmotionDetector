import  tensorflow as tf

with tf.compat.v1.Session() as sess:
        h = tf.constant("hello")
        ans = sess.run(h)
        print(ans)
