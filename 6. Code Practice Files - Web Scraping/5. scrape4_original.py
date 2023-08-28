# Scraping Flipkart Website - Using Selenium (data accessing) and BeautifulSoup (parsing HTML)
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

# You need to download the ChromeDriver here: https://chromedriver.chromium.org/
driver = webdriver.Chrome("chromedriver") # Put the path/ file location of the downloaded and extracted driver

products = []   # List to store names of the products
prices = []     # List to store prices of the products
ratings = []    # List to store ratings of the products

driver.get("https://www.flipkart.com/laptops/~buyback-guarantee-on-laptops-/pr?sid=6bo%2Cb5g&uniqBStoreParam1=val1&wid=11.productCard.PMU_V2")
content = driver.page_source
soup = BeautifulSoup(content, 'html.parser')

for each in soup.findAll('a', href=True, attrs={'class':'_1fQZEK'}): #findAll (BS version 3) == find_all (bs4)
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
df.to_csv('products3.csv', index = False)
