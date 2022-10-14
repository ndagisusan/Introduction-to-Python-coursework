import pandas as pd

df = pd.read_json('https://www.w3schools.com/python/pandas/data.js')
# Structure:
# df = {
#   'Duration': { __:__ , __:__ , __:__, ... },
#   'Pulse': { __:__ , __:__ , __:__, ... },
#   'Maxpulse': { __:__ , __:__ , __:__, ... }, 
#   'Calories': { __:__ , __:__ , __:__, ... }
# }

print(df.to_string())  # prints the entire DataFrame

print(df.head()) # Print the first 5 rows of the DataFrame
print(df.tail()) # Print the last 5 rows of the DataFrame

# Accessing columns
print(df['Duration'])

# Accessing rows
print(df.iloc[91]) # Locate row using the index

# Mean and Median
print(df['Pulse'].median())
print(df['Pulse'].mean())

# Unique values
print(df['Calories'].unique())
# OR
# print(df.Calories.unique()) # Only if there is no space in the column name

# # Histogram for visualization
# df.Calories.hist()
# df.Calories.hist(bins = 3)