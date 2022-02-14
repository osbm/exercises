import matplotlib.pyplot as plt
import numpy as np

np.random.seed(42)
y1 = np.random.normal(size=8*5)*100
y2 = np.random.normal(size=8*5)*100

y1.sort() # sort 
y2.sort()
y2 = y2[::-1] # sort and reverse

years = np.arange(1978, 2018)

plt.subplot(2,1,1)
plt.plot(years, y1, "r")

plt.subplot(2,1,2)
plt.plot(years, y2, "b")
plt.tight_layout()
plt.savefig("test5.svg")
plt.show()
