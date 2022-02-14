import numpy as np
import seaborn as sns

iris = sns.load_dataset('iris')

#print(np.mean(iris['petal_length']))
#print(np.mean(iris.iloc[:, 0:4]))
print(np.median(iris.petal_length))