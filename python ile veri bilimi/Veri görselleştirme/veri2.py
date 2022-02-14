import matplotlib.pyplot as plt
import numpy as np

np.random.seed(42)
years = np.arange(1999, 2017)
growth = np.random.random(18)

plt.plot(years, growth)
plt.xlabel("Years")
plt.ylabel("Growth")
plt.title("Test title")

plt.show()