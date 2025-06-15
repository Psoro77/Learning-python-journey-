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
# redo =True
# n = 0
# h=0
# while(redo):
#     print('please enter a integer')
#     sc =input()
#     try:
#         number =int(sc)
#         redo=False
#     except ValueError :
#         print('this is not an interger ')
#         redo= True
# # for n in range(n, number):
# #     for p in range(number-n-1):
# #         print(' ', end='')
# #     for j in range(n*2+1):
# #         print('*', end='')
# #     print('')
# #j'ai reussi a le faire assez facilement 
# # je vais essayer de faire un losange la
# for n in range(n, number):
#     for p in range(number-n-1):
#         print(' ', end='')
#     for j in range(n*2+1):
#         print('*', end='')
#     print('')
# for h in range(h, number):
#     if h == 0 :
#         continue
#     for p in range(h):
#         print(' ', end='')
#     for j in range(number*2-1-h*2):
#         print('*', end='')
#     print('')
#le losange etait un peu plus tricky mais bon c'est fait

# je vais afficher les nombre premiers

# for j in range(1, 3765):
#     prime= False
#     for k in range(1, j):
#         if ((j%k ==0 and (k==j or k==1)) or not(j%k==0)):
## explication: si le nombre est divisible par k  et que le diviseur est 1 ou lui meme  c'est bon  on continue
## de checker aussi si le nombre ne le divisise pas on continuer a checker a la fin si y'as aucun chiffre qui active
##sa on passe dans is prime le cas ou c'est faux c'est quand un nombre le divise et que il est pas 1 ou lui 
## or not devien dans ce cas False sa fait False False 
#             prime=True 
#         else : 
#             prime=False
#             break
#     if prime :
#         print(f"{j} is prime")
#c'etait pas facile je me suis bcp melanger mais je l'ai eventuellement fait
#chatgpt n'arrive pas a comprendre mon code mdrrrr
#je vais refaire les nombres premier mais avec une liste dans un array
# listnum = [22,21,1,2,3,4,99,56,7837,773,3763,892073]
# for nombre in listnum:
#     prime = True
#     for j in range(1,nombre+1):
#          if ((nombre%j ==0 and (j==nombre or j==1)) or not(nombre%j==0)):
#             prime=True 
#          else : 
#             prime=False
#             break
#     if prime :
#         print(f"{j} is prime")
#sa marche meme si l'ia dit que sa marche pas 
# en java j'avais fais 
# JOptionPane.showMessageDialog(null, "in this program we gonne check if a number is "
# 				+ " 'premier' or not ");
# 		//d'abord on va demander un nombre quelquonque et le storer dans un int
# 		// avec le JOptionPane
# 		int N =Integer.parseInt(JOptionPane.showInputDialog("please enter the number "));
# 		int i = 1;
# 		boolean premier = true;
# 		String text;
# 		for(i=1;N%i!=0&&i<=N;++i) {
			
# 			premier = true;
# 		} if (N%i!=0 && N!=i) {
# 			premier = false;
# 		} if(premier == false ) {
# 			 text ="n'est pas premier il est divisible par";
# 			 JOptionPane.showMessageDialog(null, N + " " + text + " " + i);
# 		}else {
# 			text = "est premier il n'est divisible que par 1 et lui meme";
# 			 JOptionPane.showMessageDialog(null, N + " " + text );
# 		}
		
# 	}
# }
#array part
#
listnum = [22,21,1,2,3,4,99,56,7837,5,773,3763,892073,77,1,2,77,8272,99,5,5]
# for nombre in listnum :
#     count =0
#     for i in range(len(listnum)):
#         if nombre==listnum[i]:
#             count=count+1
#     print(f"{nombre} is counted {count} times")
#ma version 
#la version chatgptienne:
#on utilise un dictionnaire ou notre nombre et la cle et le truc est la frequence si on croise on update la frequence en fesant 
#plus un
# freq ={}
# for num in listnum:
#     if num in freq :
#         freq[num]+=1
#     else:
#         freq[num]=1
# for number, frequence in freq.items():
#     print(f"{number} appears {frequence} time")
# recherche element
#
# elemnt =5
# i=0
# for number in listnum :

#     if number==elemnt :
#         print(f"element found at index : {i}")
#     i+=1
#supprimmer les doublons
# freq = {}
# for number in listnum:
#     if number in freq :
#         freq[number]+=1
#     else:
#         freq[number]=1 # je met un dictionnaire avec la frequence de chaque chiffre de la liste 

# for cle, values in freq.items() :# je check si la veuleur est superieur a un je suprimme de la liste  pour quil en reste 
#     #qu'un seul
#     if values >1    :
#         for i in range(values-1):
#             listnum.remove(cle)
# print(listnum)
#pop enleve par rapport a l'index remove enleve l'occurence de la valeur dans la liste
# programme pour demander un array et le decouper en deux
redo = True
listenc= []
def stoparr(listen):
    half= len(listen)/2
    half =int(half)
    listenc2 = listen[half:]
    listen= listen[:half]
    print(listen)
    print(listenc2)
    return
while redo:
    print('please enter a value |S to stop')
    sc =input()
    if sc ==('s' or 'S'):
        redo= False
        stoparr(listenc)
        break
    try :
        nombre =int(sc)
        listenc.append(nombre)
        redo=True
    except ValueError :
        print('this is not an integer')



    
 


        

 
