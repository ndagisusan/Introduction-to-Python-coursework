# SEABORN - PANDAS
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df2 = pd.read_csv("https://raw.githubusercontent.com/ywchiu/riii/master/data/house-prices.csv")
print(df2)
print(df2.Price.max())                  # Check max value of the Price column

# Different plots - histplot, displot, regplot, lmplot
# Seaborn Histogram
sns.histplot(df2.Neighborhood)          # Plot shows the x and y-axes label on default
plt.show()

# Displot - histogram + other plot types (More appealing plot)
sns.displot(df2["SqFt"], kde=True, bins=5, rug=True, color="purple", alpha=0.8, fill=True)          # Plot shows the x and y-axes label on default
# kde: line curve plot on top of the bar chart, bins: groupings, rug: tick marks on the x-axis
# color: color of the chart, alpha: opacity, fill: choose if the bars are to be filled with color
plt.show()

# Regplot - Scatter plot + Regression line (Trend Line)
sns.regplot(data=df2, x="Price", y="Offers")
plt.show()

# LMPLOT - more high level than than the regplot
# Can organize the data by colors(hue), columns(col), or rows(row)
# col and row produce multiple plots
sns.lmplot(data=df2, x="Price", y="Offers", hue="Brick", col="Neighborhood")
plt.xticks([0, 25000, 50000, 75000, 100000, 125000, 150000, 175000, 200000, 225000],
           ['0', '25k', '50k', '75k', '100k', '125k', '150k', '175k', '200k', '225k'])
# The above adjusts the scale to be more readable. NB: Both scales MUST be of the same length
plt.show()
plt.clf()               # Clears the current plot