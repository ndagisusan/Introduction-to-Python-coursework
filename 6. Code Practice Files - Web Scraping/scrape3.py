# Scraping Flipkart Website - Using BeautifulSoup
import requests
from bs4 import BeautifulSoup
import pandas as pd

products = [] #List to store name of the product
prices = [] #List to store price of the product
ratings = [] #List to store rating of the product

sp = requests.get("https://www.flipkart.com/laptops/~buyback-guarantee-on-laptops-/pr?sid=6bo%2Cb5g&uniqBStoreParam1=val1&wid=11.productCard.PMU_V2")
sp = BeautifulSoup(sp.content, 'html.parser')

for each in sp.find_all('a', href=True, attrs={'class':'_1fQZEK'}):
    name = each.find('div', attrs={'class':'_4rR01T'})
    price = each.find('div', attrs={'class':'_30jeq3 _1_WHN1'})
    rating = each.find('div', attrs={'class':'_3LWZlK'})

    products.append(name.text) # Get the text part
    prices.append(price.text)
    ratings.append(rating.text) 

# Structuring and storing data
df = pd.DataFrame({'Product Name': products, 'Price': prices, 'Rating': ratings}) 
print(df.to_string())

# Output the DataFrame to CSV file
# df.to_csv('products.csv', index = False)