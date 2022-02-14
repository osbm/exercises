from tensorflow import keras
import numpy as np

# This is the example code from the first week

model = keras.Sequential([keras.layers.Dense(units=1, input_shape=[1])])
model.compile(optimizer="sgd", loss="mean_squared_error")



xs = np.array([-1.0, 0.0, 1.0, 2.0, 3.0, 10.0], dtype=float)
ys = np.array([-3.0, -1.0, 1.0, 3.0, 5.0, 19.0], dtype=float) # this is a linear function y = 2x -1

model.fit(xs, ys, epochs=5000)

print(model.predict([10.0]))# the result must be 19 and it really works

