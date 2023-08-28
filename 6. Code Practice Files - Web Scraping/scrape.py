# Get S&P500 list of companies tickers from NYSE
import requests
from bs4 import BeautifulSoup

# The above is similar to the breakdown below:
# import numpy - numpy.array
# import numpy as np - np.array
# from numpy import array - array

sp = requests.get("https://en.wikipedia.org/wiki/List_of_S%26P_500_companies") # Sends a GET request to the specified URL - fetches the website
# print(sp) # Status code
sp = BeautifulSoup(sp.content, 'html.parser') # content - Returns the content of the response, in bytes, after which data can be pulled out of the HTML file
# print(sp) # The page source code

# Empty list initialized
SP500 = []

for each in sp.find_all('a', href = True): # Find all <a> components and look for href in them
    if 'nyse.com' in each.get('href'): # Check if nyse.com is part of the link
        SP500.append(each.get('href').split("XNYS:")[1].upper()) # Extract the end of it
    if len(SP500) == 50:
        break

print(SP500)