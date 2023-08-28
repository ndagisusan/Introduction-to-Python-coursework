# Scraping Flipkart Website - Using BeautifulSoup
import requests
from bs4 import BeautifulSoup
import pandas as pd

products = []   # List to store names of the products
prices = []     # List to store prices of the products
ratings = []    # List to store ratings of the products

sp = requests.get("https://www.flipkart.com/laptops/pr?sid=6bo,b5g&marketplace=FLIPKART")
sp = BeautifulSoup(sp.content, 'html.parser')

for each in sp.find_all('a', href=True, attrs={'class':'_1fQZEK'}):
    name = each.find('div', attrs={'class':'_4rR01T'})
    price = each.find('div', attrs={'class':'_30jeq3 _1_WHN1'})
    rate = each.find('div', attrs={'class':'_3LWZlK'})

    products.append(name.text)   
    prices.append(price.text)
    ratings.append(rate.text) 

# Structuring and storing data
df = pd.DataFrame({'Product Name': products, 'Price': prices, 'Rating': ratings}) 
print(df.to_string())

# Output the DataFrame to CSV file
df.to_csv('products.csv', index = True)
