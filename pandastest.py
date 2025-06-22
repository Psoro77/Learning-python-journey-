import pandas as pd
datas = {
    'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}
myvar = pd.DataFrame(datas)

print(myvar)
a = [1, 7, 2]

myvar = pd.Series(a)

print(myvar)
data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

myvar = pd.DataFrame(data)

print(myvar)
teill= {
    'jus': ['jus de pomme', 'jus d orange', 'jus de raisin'],
    'alcool': ['hennesy', 'vody', 'chateaurouge']
}
bouteille = pd.DataFrame(teill, index=['classe1','classe eco', 'vip'])
print(teill)
print(bouteille)
#we can load file into a data fame 
avion = pd.read_csv("C:/Users/USER/Downloads/airtravel.csv")
print('')
print(avion.head(10))
print(avion.info())