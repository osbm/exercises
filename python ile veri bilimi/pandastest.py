import pandas as pd 
import numpy as np
mydict = {
    "first_name": ("osman", "faruk", "sebastian", "kyle", "rick"),
    "last_name": ["McFarlene", "Lague", "Clark", "Holmes", "Sanchez"],
    "age": np.array([20, 45, 26, 66, 10]),
    "weight": pd.Series([60, 70, 80, 30, 10])
}

frame = pd.DataFrame(mydict)
print(frame)