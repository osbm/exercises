from sklearn.metrics import mean_squared_error
# mean_squared_error(squared=False)


import numpy as np
def rmse(predictions, targets): # quick simple
    return np.sqrt(((predictions - targets) ** 2).mean())


# same but easy to understand
def root_mean_square_error(predictions: np.array, targets: np.array) -> np.float64:
    error = predictions - targets
    square_error = error ** 2
    mean_square_error = square_error.mean()
    return np.sqrt(mean_square_error)
    
print(root_mean_square_error(np.array([1,1,1,1]), np.array([1,1,1,1])))  # 0.0
print(root_mean_square_error(np.array([1,1,1,1]), np.array([2,2,2,2])))  # 1.0
print(root_mean_square_error(np.array([1,1,1,1]), np.array([2,2,2,20]))) # 9.53




