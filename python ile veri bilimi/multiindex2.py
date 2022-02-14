import pandas as pd
import numpy as np

indexes = pd.MultiIndex.from_product([["ABC", "DEF", "KLM"], ["2016", "2017"]])
colums = pd.MultiIndex.from_product([["Q1", "Q2", "Q3", "Q4"], ["Hacim", "Kapanış"]])

data = np.arange(1, 49)
np.random.shuffle(data)
data = np.reshape(data, (6,8))

trades = pd.DataFrame(data, index=indexes, columns=colums)
print(trades.iloc[2])
# print(trades.to_html())

#mySeries = pd.Series([1,2,3,4,5], index=indexes)
#print(mySeries.unstack())