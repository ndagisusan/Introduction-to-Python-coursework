# Scraping Flipkart Website - Using Selenium (data accessing) and BeautifulSoup (parsing HTML)
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

driver = webdriver.Chrome() # No need to download the driver and input its file path

products = []   # List to store names of the products
prices = []     # List to store prices of the products
ratings = []    # List to store ratings of the products

driver.get("https://www.flipkart.com/laptops/pr?sid=6bo,b5g&marketplace=FLIPKART")
content = driver.page_source
soup = BeautifulSoup(content, 'html.parser')

for each in soup.findAll('a', href=True, attrs={'class':'_1fQZEK'}): #findAll (BS version 3) == find_all (bs4)
    name = each.find('div', attrs={'class':'_4rR01T'})
    price = each.find('div', attrs={'class':'_30jeq3 _1_WHN1'})
    rate = each.find('div', attrs={'class':'_3LWZlK'})

    if name is None:    # Caters for instances where the name does not exist
        products.append(None)
    else:
        products.append(name.text) # Get the text part

    if price is None:
        prices.append(None)
    else:
        prices.append(price.text)

    if rate is None:    # Caters for instances where the rating does not exist - which was causing an error initially
        ratings.append(None)
    else:
        ratings.append(rate.text)

# Structuring and storing data
df = pd.DataFrame({'Product Name': products, 'Price': prices, 'Rating': ratings}) 
print(df.to_string())

# Output the DataFrame to CSV file
df.to_csv('products4.csv', index = False)
