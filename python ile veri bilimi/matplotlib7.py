import pandas as pd
import matplotlib.pyplot as plt

tesla = pd.read_csv('TSLA.csv')
#plt.plot(tesla['Close'])
tesla['Close'].plot() # both works
plt.savefig('test7.svg')
plt.show()