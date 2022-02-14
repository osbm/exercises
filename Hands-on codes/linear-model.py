import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import sklearn.linear_model

import numpy as np
import matplotlib.pyplot as plt
n=50
x=np.linspace(-3,3,n)
y=np.linspace(-3,3,n)
X,Y=np.meshgrid(x,y)
# vector field
u=np.cos(X+Y)
v=np.sin(X-Y)
# plot
plt.streamplot(X, Y, u, v, density=2)
plt.show()


