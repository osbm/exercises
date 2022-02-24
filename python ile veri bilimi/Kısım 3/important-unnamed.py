from sklearn.datasets import load_boston
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

boston = load_boston()
boston_df = pd.DataFrame(boston.data, columns=boston.feature_names)
boston_df['MEDV'] = boston.target

plt.scatter(boston_df['LSTAT'], boston_df['MEDV'], label="veriler", color="black", marker="o", alpha=0.4)
sns.regplot(x="LSTAT", y="MEDV", data=boston_df, scatter=None, order=1, color="red", label="1. dereceden polinom")
sns.regplot(x="LSTAT", y="MEDV", data=boston_df, scatter=None, order=2, color="blue", label="2. dereceden polinom")
sns.regplot(x="LSTAT", y="MEDV", data=boston_df, scatter=None, order=3, color="green", label="3. dereceden polinom")

plt.legend(loc="upper right")
plt.show()