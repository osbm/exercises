import seaborn as sns
import pandas as pd
iris = sns.load_dataset("iris")

#print(iris.count())
#print(iris.describe().to_html())
#print(iris["species"].unique())

#with open("iris.html", "w") as file:
#    file.write(iris.to_html())

#print(iris["species"].unique())
"""
filter1 = iris["sepal_length"] > 6.5
filter2 = iris["sepal_length"] < 7.5
print(iris[filter1 & filter2].head())"""
"""
filter = iris["species"].str.startswith("versi") # versicolor
print(iris[filter].head())
"""
print(iris.petal_length[iris.sepal_length > 7.5])

"""

result = []
for data in pd.read_csv("data.csv", chunksize=100):
    result.append(data["A"])


"""