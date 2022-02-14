import matplotlib.pyplot as plt
import numpy as np

np.random.seed(42)
y1 = np.random.rand(8*5)*100
y2 = np.random.rand(8*5)*100

y1.sort() # sort 
y2.sort()
y2 = y2[::-1] # sort and reverse

years = np.arange(1978, 2018)

plt.plot(years, y1, "r")
plt.plot(years, y2, "b")
plt.savefig("test2.svg")
plt.show()