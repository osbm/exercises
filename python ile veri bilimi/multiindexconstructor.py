import pandas as pd
from pandas.core.indexes.multi import MultiIndex

print(pd.MultiIndex.from_tuples([
    ("x", 1),
    ("x", 2),
    ("y", 1),
    ("y", 2),
]))

print(pd.MultiIndex.from_arrays([
    ["x", "x", "y", "y"],
    [1, 2, 1, 2]
]))

print(pd.MultiIndex.from_product([
    ["x", "y"],
    [1, 2]
]))