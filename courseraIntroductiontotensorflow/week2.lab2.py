
import tensorflow as tf
# GRADED FUNCTION: train_mnist
def train_mnist():
    # Please write your code only where you are indicated.
    # please do not remove # model fitting inline comments.

    # YOUR CODE SHOULD START HERE
    class myCallback(tf.keras.callbacks.Callback):
      def on_epoch_end(self, epoch, logs={}):
        if(logs.get('accuracy')>0.99):
          print("Reached 99% accuracy so cancelling training!")
          self.model.stop_training = True

    callbacks = myCallback()
    # YOUR CODE SHOULD END HERE

    mnist = tf.keras.datasets.mnist

    (x_train, y_train),(x_test, y_test) = mnist.load_data(
    )
    # YOUR CODE SHOULD START HERE
    x_train = y_train / 255.0
    x_test = y_test / 255.0
    # YOUR CODE SHOULD END HERE
    model = tf.keras.models.Sequential([
        # YOUR CODE SHOULD START HERE
        tf.keras.layers.Flatten(),
        tf.keras.layers.Dense(512, activation=tf.nn.relu),
        tf.keras.layers.Dense(10, activation=tf.nn.softmax)
        # YOUR CODE SHOULD END HERE
    ])

    model.compile(optimizer='adam',
                  loss='sparse_categorical_crossentropy',
                  metrics=['accuracy'])
    
    # model fitting
    model.fit(
        # YOUR CODE SHOULD START HERE
        x_train, y_train, epochs=10, callbacks=[callbacks]
        # YOUR CODE SHOULD END HERE
    )
    # model fitting
    model.evaluate(x_test, y_test)


print(train_mnist())