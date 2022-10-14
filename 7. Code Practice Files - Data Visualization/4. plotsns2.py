# SEABORN - Comparing different plots
from matplotlib import pyplot as plt
import seaborn as sns
import pandas as pd

df2 = pd.read_csv("https://raw.githubusercontent.com/ywchiu/riii/master/data/house-prices.csv")

plt.figure(1)
sns.displot(df2.SqFt, kind='hist')      # Requires Numeric data

plt.figure(2)
sns.displot(df2.SqFt, kind='kde')       # Requires Numeric data

plt.figure(3)
sns.displot(df2.SqFt, kind='ecdf')      # Requires Numeric data

# Seaborn histogram vs Pandas histogram
plt.figure(5)

plt.subplot(121)
sns.histplot(df2.Price)          # Plot shows the x and y-axes label on default

plt.subplot(122)
df2.Price.plot.hist()            # Requires Numeric data
plt.show()                       # Shows all plots at once, as different figures

# What differences do you see??