# i will learn loop in this file
# 
n =20
#for i in range(1, n):
 #   print(i)
# sa printe de index 1 a n-1
#for i in range(n):
#    print(i)
#    i=i+1
i=0
# for i in range(i, n , 2):
#     print(i)
#     i=+1
#print i à n en sautant d'e deux
# for i in range(n, i, -5):
#   print(i)
#si je fais  ordre decrosisant en enlveant 5 a chaque pas  sa print 20 15 10 5 
# sa prend le i  initian dans la condition
mot = "rfyvhbjv"
# for lettre in mot:
#     print(lettre)
#en gros c comme une boucle foreach sur php il itere sur chaque element de la boucle
listest = ['banane', 'pomme', 'poire', 'fraise', 'pineaple']
# for mott in listest :
#     print(mott)
# for i in range (len(listest)-1, i , -2):
#     print(f"{i}: {listest[i]}")
#je vais dessiner un triangle d'etoile avec l'input de l'user
# je vais afficher les nombre premiers
redo =True
n = 0
h=0
while(redo):
    print('please enter a integer')
    sc =input()
    try:
        number =int(sc)
        redo=False
    except ValueError :
        print('this is not an interger ')
        redo= True
# for n in range(n, number):
#     for p in range(number-n-1):
#         print(' ', end='')
#     for j in range(n*2+1):
#         print('*', end='')
#     print('')
#j'ai reussi a le faire assez facilement 
# je vais essayer de faire un losange la
for n in range(n, number):
    for p in range(number-n-1):
        print(' ', end='')
    for j in range(n*2+1):
        print('*', end='')
    print('')
for h in range(h, number):
    if h == 0 :
        continue
    for p in range(h):
        print(' ', end='')
    for j in range(number*2-1-h*2):
        print('*', end='')
    print('')