# MATPLOTLIB - PANDAS
import matplotlib.pyplot as plt
import pandas as pd

# Read from CSV file
df = pd.read_csv('https://www.w3schools.com/python/pandas/data.csv')

# df2 = pd.read_csv('https://raw.githubusercontent.com/ywchiu/riii/master/data/house-prices.csv')       
# You can practice with this DataFrame as well and try to make sense of the data

# Dataframe format
# df = {
#   'Duration': [ __ , __ , __, ... ],
#   'Pulse': [ __ , __ , __, ... ],
#   'Maxpulse': [ __ , __ , __, ... ], 
#   'Calories': [ __ , __ , __, ... ]
# }

# Checking your Data Frame values
# print(df)                                          # Prints the first 5 and the last 5 rows of the Data Frame
# print(df.head())                                   # Prints the first 5 rows of the Data Frame
print(df.to_string())                              # Prints the entire Data Frame - all rows

# Different plots - scatter, hist
# 1. SCATTER
# Labels
plt.xlabel("Pulse")
plt.ylabel("Calories")
plt.title("Calories against Pulse")

plt.scatter(df.Pulse, df.Calories, marker="*", s=df.Duration)    # Line graph - The labels above apply for this plot only
# s: size of marker (In this example, the size of marker matches the Duration)
# plt.yscale('log')                                    # Logarithmic Scale: Used if the values in the chart cover a very large range
plt.text(270, 1729, 'Highest')
plt.text(15, 50.5, 'Lowest')

plt.show()                 # Displays the plot


# 2. HISTOGRAM - Explores the dataset and gives the idea of the distribution
# Ticks - Defines your scales
plt.xticks([0, 30, 60, 90, 120, 150, 180, 210, 240, 270, 300])
plt.yticks([0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100])

# Labels
plt.xlabel("Duration")
plt.ylabel("Count")
plt.title("Count against Duration")

df.Duration.hist()                  # Histogram: Default bins = 10. Can specify the number of bins using the bins parameter
# Has default gridlines added
# Or df["Duration"]hist()           
plt.show()                          # The ticks and labels above apply for this plot only

df.Duration.hist(bins=5)            # Too few bins oversimplify your reality, Too many bins overcomplicate it
plt.show()                          # No ticks or labels on this plot
plt.clf()                           # Clears the current plot

# Pandas histogram
df.Duration.plot.hist(bins=3)       # No grid lines on the plot
# plt.grid(True)                      # Adds the grid lines
plt.show()

