import pandas as pd
import numpy as np

indexes = pd.MultiIndex.from_product([["ABC", "DEF", "KLM"], [2016, 2017]])
colums = pd.MultiIndex.from_product([["Q1", "Q2", "Q3", "Q4"], ["Hacim", "Kapanış"]])

data = np.arange(1, 49)
np.random.seed(42)
np.random.shuffle(data)
data = np.reshape(data, (6,8))

trades = pd.DataFrame(data, index=indexes, columns=colums)

#print(trades)
#print(trades.to_html())
#print(trades["Q1"].to_html())
#print(trades.loc["ABC"].to_html())
#print(trades.loc[["ABC", "DEF"], ["Q3", "Q4"]].to_html())


"""
for a in trades:
    print(a, type(a))
input()
for index, column in trades.iteritems():
    print(index, "and", column)
input()

    
for index, row in trades.iterrows():
    print(index, "and", row)
"""

print(trades.describe())