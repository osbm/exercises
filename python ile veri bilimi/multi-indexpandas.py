import numpy as np
import pandas as pd

indexes = [
    ("Yakuza", 2017),
    ("Yakuzam", 2018),
    ("Yakuzamsı", 2019),
    ("Yakuzamtırak", 2020),
    ("Yakuzalı", 2021),

    ("Yakuzacı", 2017),
    ("Yakuzasız", 2018),
    ("Yakuzacık", 2019),
    ("Yakuzacağız", 2020),
    ("Yakuzala", 2021)
]
index = pd.MultiIndex.from_tuples(indexes)
index.set_names(["Yakuza type", "Year"], inplace=True)

mySeries = pd.Series(np.random.uniform(0, 50, 10), index=index)
print("Before:")
print(mySeries)
print("After:")
print(mySeries.unstack())