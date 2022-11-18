import pandas as pd

# SERIES - Column
# List
# Printing & subsetting using index
a = [1, 7, 2]
myvar = pd.Series(a)
print(myvar)
print(myvar[0], '\n') # Subsetting using indices
# OR
# Printing and Subsetting using labels
myvar = pd.Series(a, index = ['a', 'b', 'c'])
print(myvar)
print(myvar['b'], '\n') # Subsetting using indices

# Dictionary - printing & subsetting using KEY
calories = {"day1": 420, "day2": 380, "day3": 390} # Key:Value pairs
myvar1 = pd.Series(calories)
print(myvar1)
print(myvar1["day1"])


# EXAMPLE 2
# List
ages = [14, 52, 56, 25, 69]
# Using Labels
pd_ages = pd.Series(ages, index = ['a', 'b', 'c', 'd', 'e'])
print(pd_ages)

# Subsetting
print(ages[2:4]) # list - [56, 25]
print(pd_ages[2:4]) # pandas series - subset using index
# print(pd_ages['c':'e']) # pandas series - subset using labels

# Dictionary
ages_dict = {"John": 14,"Jane": 25,"Simon": 56, "Alex":25,"Jennifer": 69} # Key:Value pairs
pd_ages_dict = pd.Series(ages_dict)
# pd_ages_dict = pd.Series(ages_dict, index = ['a', 'b', 'c', 'd', 'e']) - Cannot use labels for dictionaries as the KEY is used for subsetting

print(pd_ages_dict)
