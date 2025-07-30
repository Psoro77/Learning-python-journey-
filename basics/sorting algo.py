#in this file i am going to try to create some sorting algorith by my own to understant more array in python
#and loops and keys ect so im going to create some function and just ask the user for a method to use and also for some 
#input
import sys
mylist = []
def askinput ():
    print('please enter some number enter s To stop the input')
    inp = input()
    if inp == "s" or inp =='S' :
        if len(mylist)<=0 :  #check if the list is blank if its the case ask again w recursive call
            askinput()
        else : 
            askmethod()
        return
    try :
        number = float(inp)         #try if the input can convert to a float if it cannot throw error
        mylist.append(number)
        askinput() ## to do the loop i do a recursive call
    except ValueError:
        print("that was not a number")
        askinput()    # to loop over i do a rec call

def askmethod():
    print('please choose a method of sorting')
    print("sorted | Selection sort | Buble sort | merge sort | quick sort")
    meth = input().lower()
    if 'sorted'in meth:
        print('going sorted....')
        list2  = sorted(mylist)
        print('sorted list :', list2)
        return
    elif 'selection'in meth:
        list2 = selection(mylist)
        print('Selection    sorted list :', list2)
        return
    elif 'buble'in meth:
        list2 = buble(mylist)
        print(f"Buble sorted list :{list2}")

        
        return
    elif 'merge'in meth:
        list2 = merge(mylist)
        print(list2)
        return
    elif 'quick'in meth:
        quick()
        return
    else :
        askmethod() # recursive call if we dont find a match
    return

def selection(mylist):
    # for i in range(len(mylist)) : #passer a travers tout les elemet de la liste
    #     j=i                         #a chaque iteration je reset j a i pour progresser dans la liste
    #     for j in range(len(mylist)): #de l'element precedent a la fin de la liste
    #         if mylist[j] > mylist[i]: #si l'element courant est plus grand on les swapp apres sa l'element
    #             #suivant on regarde encore
    #             mylist[j], mylist[i]= mylist[i], mylist[j]
    # return mylist
    #le selection sort checherche le minimum du array et le remplace par le i present
    for i in range(len(mylist)):
        min=i
        for j in range(i, len(mylist)):
            if mylist[min]<mylist[j]:
                min=j
        mylist[min], mylist[i]= mylist[i], mylist[min]
    return mylist
def buble(mylist):
    flag = True
    while flag :
        flag=False
        for j in range(1, len(mylist)):
            if mylist[j-1]>mylist[j] :
                mylist[j], mylist[j-1]= mylist[j-1], mylist[j]
                flag =True
    return mylist
#j'ai enfin reussi
def merge(mylist):
        if len(mylist) ==1 :
            return mylist
        else :
            mid = len(mylist)//2
            larr= mylist[:mid]
            rarr = mylist[mid:]
            L1 = merge(larr)
            R2 =merge(rarr)
            return sorting(L1, R2)
        
        
def sorting(L1arr, R2arr):
    result =[]
    l = r =0
    while (l < len(L1arr) and r < len(R2arr)):
        if L1arr[l]<R2arr[r]:
            result.append(L1arr[l])
            l+=1
        else:
            result.append(R2arr[r])
            r+=1
    result.extend(L1arr[l:])
    result.extend(R2arr[r:])
    return result



askinput() 
