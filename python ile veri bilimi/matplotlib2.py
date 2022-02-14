import matplotlib.pyplot as plt
import numpy as np

np.random.seed(42)
y1 = np.random.normal(size=8*5)*100
y2 = np.random.normal(size=8*5)*100

y1.sort() # sort 
y2.sort()
y2 = y2[::-1] # sort and reverse

years = np.arange(1978, 2018)
plt.axes([0.05, 0.05, 0.4, 0.9])
plt.plot(years, y1, "r")
plt.axes([0.55, 0.05, 0.4, 0.9])
plt.plot(years, y2, "b")
plt.savefig("test.svg", tranparent=True)
plt.show()