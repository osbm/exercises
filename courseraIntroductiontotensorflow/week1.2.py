from tensorflow import keras
import numpy as np
import tensorflow as tf

fashion_mnist = keras.datasets.fashion_mnist

(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()

#normalizing 
train_images = train_images / 255.0
test_images  = test_images  / 255.0


model = keras.Sequential([
    keras.layers.Flatten(input_shape=(28, 28)),
    keras.layers.Dense(128, activation=tf.nn.relu),
    keras.layers.Dense(128, activation=tf.nn.relu),
    keras.layers.Dense(10, activation=tf.nn.softmax)
])

model.compile(
    optimizer = tf.optimizers.Adam(),
    loss = "sparse_categorical_crossentropy"
)

model.fit(train_images, train_labels, epochs=5)
input()
model.evaluate(test_images, test_labels)