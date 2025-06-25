import pandas as pd
import matplotlib.pyplot as mat
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
ds1g =  ds.sort_values("Speed", ascending=False)[ds ["#"] <152]
print("in the first gen the 20 fastest are ")
print(ds1g.head())
ds1g= ds1g.head(10)
ds1g.set_index("Name", inplace=True)
ds1g.plot.bar()

mat.title("Les 10 pokemons les plus rapides de la gen 1")
mat.ylabel("stat")
mat.xlabel("pokemon")
mat.show()

#montrer la distribution de la vitesse
ds1g["Speed"].hist(bins=10, figsize=(10, 6), color="orange", edgecolor="black")
mat.title("Distribution des vitesses")
mat.xlabel("Vitesse")
mat.ylabel("Nombre de Pokémon")
mat.show()