
from tensorflow import keras
import numpy as np

# GRADED FUNCTION: house_model
def house_model(y_new):
    values = [float(x) for x in range(10)]
    print(values)
    # i am not giving the test value in here
    xs = np.array(values, dtype=float)# i am not giving the test value in here
    ys = 50_000*xs + 50_000  # i am applying the function y = 50000x + 50000 right here
    model = keras.Sequential([keras.layers.Dense(units=1, input_shape=[1])])
    model.compile(optimizer="sgd", loss="mean_squared_error")
    model.fit(xs, ys, epochs=5000)
    return model.predict(y_new)[0][0]

prediction = house_model([7.0])
print(prediction)