import random
nombre_secret = random.randint(1, 100)
essais =-1
print('please enter a number between 1 and a 100')
numbertried =0
while numbertried!=nombre_secret :
    essais+=1
    numbertried =int(input())
    refaire = True
    while refaire:
        if numbertried < 0 :
            print('a number between 1 and a 100 please')
            numbertried =int(input())
            refaire =True
        elif numbertried>100 :
            print('a number between 1 and a 100 please')
            numbertried =int(input())
            refaire = True
        else :
            refaire = False
    if numbertried < nombre_secret :
        if numbertried-nombre_secret<-30:
            print("the actual number is way over")
        elif numbertried-nombre_secret<-20:
            print("the actual number is over")
        elif numbertried-nombre_secret<-10:
            print("the actual number is a little bigger")
        else :
            print("you are close")
    if numbertried > nombre_secret :
        if numbertried-nombre_secret>30:
            print("the actual number is way below")
        elif numbertried-nombre_secret>20:
            print("the actual number is below")
        elif numbertried-nombre_secret>10:
            print("the actual number is a little smaller")
        else :
            print("you are close")
print("You guessed in {} tries".format(essais))

