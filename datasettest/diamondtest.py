import pandas as pd 
import matplotlib as plt
 
url = "https://gist.githubusercontent.com/sarchak/b87ad2be315ce05f7a047550646f3c41/raw/0c7d83608111f74f212398fc0d2a704e4f8dc499/diamonds.csv"
ds = pd.read_csv(url)
print("10 diamonds",ds.head(10))
print("the average price of a diamond is ",ds["price"].mean())
print(f"the more expensive diamond is { ds['price'].max()} $")
