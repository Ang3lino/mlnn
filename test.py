
tf.reset_default_graph()

X = tf.placeholder("float")
Y = tf.placeholder("float")

# tf.Variable(val, name)
a = tf.Variable(0.0)
b = tf.Variable(0.0)
c = tf.Variable(0.0)

# predicted = tf.add(tf.multiply(X, W), b)
# ax**2 + bx + c
predicted = tf.add(tf.multiply(a, tf.pow(X, 2)), tf.add(tf.multiply(b, X), c))
loss = tf.reduce_sum(tf.pow(predicted - Y, 2)) / train_n_samples
learning_rate = 0.05

# The optimizer is the gradient descent
# It uses as input parameter the learning rate and the loss function
optimizer = tf.train.GradientDescentOptimizer(learning_rate).minimize(loss)

#gpu_options = tf.GPUOptions(per_process_gpu_memory_fraction=0.3)
init = tf.global_variables_initializer()

# Number of iterations for the learning algorithm
training_epochs = 1000
display_step = 50
perm = np.random.permutation(train_n_samples)

mini_batch_size = 6
n_batch = train_n_samples // mini_batch_size + (train_n_samples % mini_batch_size != 0)
error = []

# Start training
with tf.Session(config=tf.ConfigProto(allow_soft_placement=True, log_device_placement=True)) as sess:

    # Run the initializer
    sess.run(init)

    # Fit the training data in the batches.
    for epoch in range(training_epochs):
        i_batch = (epoch % n_batch)*mini_batch_size
        batch = train_sel_feature[i_batch:i_batch+mini_batch_size], train_target[i_batch:i_batch+mini_batch_size]
        sess.run(optimizer, feed_dict={X: batch[0], Y: batch[1]})
        
        #for (x, y) in zip(train_sel_feature[perm,:], train_target[perm]):
        #    sess.run(optimizer, feed_dict={X: x, Y: y})

        # Display logs per epoch step
        if (epoch+1) % display_step == 0:
            cost = sess.run(loss, feed_dict={X: train_sel_feature, Y: train_target})
            error.append(cost)        
            print("Epoch:", '%04d' % (epoch+1), "cost=", "{:.9f}".format(cost),  "W=", sess.run(W), "b=", sess.run(b))
                  
       
   
    training_loss = sess.run(loss, feed_dict={X: train_sel_feature , Y: train_target})
    print("Training loss=", training_loss, "W=", sess.run(W), "b=", sess.run(b), '\n')
   
    
    # Visualization of the prediction for the test data
    plt.plot(test_sel_feature, test_target, 'b.', label='Original data')
    plt.plot(test_sel_feature, sess.run(W) * test_sel_feature + sess.run(b),'om', label='tensorflow LR')
    #plt.plot(test_sel_feature,predicted_test_target,'vr', label='Scikit-learn LR')
    plt.xlabel('Voice feature')
    plt.ylabel('Response variable ')

    plt.legend()
    plt.show()
