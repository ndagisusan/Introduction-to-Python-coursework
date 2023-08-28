# From API - https://www.alphavantage.co/documentation/
import requests
import pandas as pd

# replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey=demo'
r = requests.get(url)
data = r.json() #JSON format

# Structuring and storing data
pd_data = pd.DataFrame(data)
print(pd_data.to_string())