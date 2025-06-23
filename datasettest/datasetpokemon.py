import pandas as pd
url = "https://raw.githubusercontent.com/KeithGalli/pandas/master/pokemon_data.csv"
ds = pd.read_csv(url)
print(ds.head())
print(ds.columns )
print(ds.info())
dscroissant = ds.sort_values("Speed", ascending=False) 
print(dscroissant.head(50))#print the 50 fastest pokemon including the legendary

dscroissant = dscroissant[dscroissant ["Legendary"] == False]
dscroissant =dscroissant.drop("Legendary", axis=1 )
print(dscroissant.head(20)) ## showing the 20 fastest pokemon non leg