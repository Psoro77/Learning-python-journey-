import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np

url = "https://raw.githubusercontent.com/datasciencedojo/datasets/refs/heads/master/titanic.csv"
pd.set_option('display.max_columns', None)
df = pd.read_csv(url)
print(df.shape) #(891, 12)
#df.dropna(inplace= True) too many pages dropped gota drop by table
#print(df.shape)#(183, 12)
df = df.drop_duplicates()
print(df.shape) #(891, 12) no dupl
df['Fare']= df['Fare'].fillna(df['Fare'].mean() )
df =df.rename(columns={'PassengerId':'Id'})
df = df.set_index("Id")
print(df.head(5))

correfage = df['Age'].corr(df['Fare'])
print('correlation of the age and the fare', correfage )

correfare = df['Age'].corr(df['Survived'])
print('correlation of the age and the survive', correfare )

correfare = df['Fare'].corr(df['Survived'])
print('correlation of the fare and the survive', correfare )
#correlation of the fare and the survive 0.25730652238496227
corrclass = df['Pclass'].corr(df['Fare'])
print('correlation of the class and the Fare', correfare )
#correlation of the class and the Fare 0.25730652238496227 resultat logique
corrclass = df['Pclass'].corr(df['Survived'])
print('correlation of the class and the survived', correfare )
#correlation of the class and the survived 0.25730652238496227 logique aussi 


df2=df.dropna(subset=['Cabin'])
print(df2.shape) #(204, 11)
correfare = df2
df2['Fare'].corr(df['Survived'])
print('correlation of the fare and the survive 2', correfare ) 
#correlation of the fare and the survive 2 0.12830590215843232
#with this limited datased the result are less acurate
correfage = df2['Age'].corr(df2['Fare'])
print('correlation of the age and the fare', correfage )

#------------------------------------------------------------------------------------------------------------------
modeage= df['Age'].mode() 
medage= df['Age'].median()
min= df['Age'].min()
print('the more present age is', modeage)
print('the median age is', medage)
print('the yougest was ', min*12, 'month old')
#---------------------------------------------------------------------------------------------------------------
#visualisation des données 
#creer un subdf ave les donnes qui m'interessent 
dfvisu1= df.loc[:, ['Fare', 'Survived','Pclass', 'Age']]
dfvisu2 = df.loc[:,['Pclass', 'Survived']]
dfvisu3 =df.loc[:,['Age', 'Survived']]
print(dfvisu1.head(5))
dfvisu1.plot(kind= 'scatter', x='Survived', y='Fare')
plt.title("correlation of fare and survived :")
plt.show()

dfvisu2.plot(kind= 'scatter', x='Survived', y='Pclass')
plt.title("correlation of fare and survived :")
plt.show()

dfvisu3.plot(kind= 'scatter', x='Survived', y='Age')
plt.title("correlation of fare and survived :")
plt.show()
dfvisu1.plot(kind= 'scatter', y='Fare', x='Age')
plt.title("correlation of fare and survived :")
plt.show()
corrmatrix = dfvisu1[['Survived', 'Fare', 'Age','PclassS']].corr()
print(corrmatrix,'the correlation matrice result')