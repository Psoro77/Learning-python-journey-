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
   
        

 
