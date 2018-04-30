import tensorflow as tf
import numpy as np


class MODEL(object):
    def __init__(self, config): 
        self.lr = config['lr']
        self.check_iter = config['check_iter']
        self.total_iter = config['total_iter']

        self.train_x = config['train_x']
        self.train_y = config['train_y'] 
        self.val_x = config['val_x'] 
        self.val_y = config['val_y'] 
        self.eval_x = config['eval_x'] 
        self.eval_y = config['eval_y'] 

        self.num_features = config['num_features']
        self.num_champions = config['num_champions']

        self.sess = config['sess']

        self.x = tf.placeholder(shape=[None, config['num_features']], dtype=tf.float32, name='data')
        self.y = tf.placeholder(shape=[None, config['num_champions']], dtype=tf.float32, name='labels')

    def build_model(self):
        w = tf.Variable(tf.zeros([self.num_features, self.num_champions]))
        b = tf.Variable(tf.zeros([self.num_champions]))
        
        k = tf.matmul(self.x, w) + b 

        self.prediction = tf.nn.softmax(tf.matmul(self.x, w) + b)
        self.loss = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits = k, labels = self.y))
        
        self.optimize = tf.train.GradientDescentOptimizer(self.lr).minimize(self.loss)

        print("model_built")

    def run(self):
        self.sess.run(tf.global_variables_initializer())

        self.step_min = 0
        self.loss_min = float('inf')

        for i in range(self.total_iter):
            _ = self.sess.run([self.optimize], feed_dict={self.x: self.train_x, self.y: self.train_y})

            if (i + 1) % self.check_iter == 0:
                train_loss = self.sess.run(self.loss, feed_dict={self.x: self.train_x, self.y: self.train_y})
                eval_loss = self.sess.run(self.loss, feed_dict={self.x: self.eval_x, self.y: self.eval_y})

                print("-----------------------------------------------------------------------------")

                if eval_loss < self.loss_min:
                    self.loss_min = eval_loss
                    self.step_min = i+1

                    print("MIN_test_loss is updated, lr: %f" %self.lr)

                print("Step:%6d,      Train loss: %.3f" %(i+1, train_loss))
                #print("Step:%6d,      Eval  loss: %.3f" %(i+1, eval_loss))

        print("=============================================================================")
        print("=====================           RESULT        ===============================")
        print("Step:%6d,      Eval RMSE: %.3f" % (self.step_min, self.loss_min))
