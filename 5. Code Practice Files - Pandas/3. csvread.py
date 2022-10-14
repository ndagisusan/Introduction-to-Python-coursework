import pandas as pd

new_df = pd.read_csv('https://www.w3schools.com/python/pandas/data.csv')
# new_df = pd.read_csv('data.csv') # Reading files locally (File location or Filename only(if file is saved in the same location as this program))

# Structure:
# new_df = {
#   'Duration': [ __ , __ , __, ... ],
#   'Pulse': [ __ , __ , __, ... ],
#   'Maxpulse': [ __ , __ , __, ... ], 
#   'Calories': [ __ , __ , __, ... ]
# }

print(new_df) #If you have a large DataFrame with many rows, Pandas will only return the first 5 rows, and the last 5 rows
print(new_df.to_string())  # prints the entire DataFrame

print(pd.options.display.max_rows) # If the DataFrame contains more than this number of rows, the print(df) statement will return only the headers and the first and last 5 rows.

pd.options.display.max_rows = 200
print(new_df)


## EXAMPLE 2
df2 = pd.read_csv('https://raw.githubusercontent.com/ywchiu/riii/master/data/house-prices.csv')

print(df2.to_string())
print(df2.Neighborhood.unique())