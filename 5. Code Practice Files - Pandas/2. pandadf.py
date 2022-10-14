import pandas as pd

# Data Frame - 2D data structure (Table)
mydataset = {
  'cars': ["BMW", "Volvo", "Ford", "Mercedes", "Toyota"],
  'passings': [3, 7, 2, 4, 16]
}

df = pd.DataFrame(mydataset)
print(df, '\n')

df = pd.DataFrame(mydataset, index = ['i', 'ii', 'iii', "iv", "v"])
print(df, '\n')

#Subsetting in a dataframe
print(df.loc["iii"]) # Locate row using the label
print(df.loc["ii":"iv"]) # Locate rows