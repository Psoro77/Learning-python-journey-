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
    print("sorted | Selection sort | Buble sort | insertion sort | quick sort")
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
        print('Buble sorted list :', list2)
        buble()
        return
    elif 'insertion'in meth:
        insertion()
        return
    elif 'quick'in meth:
        quick()
        return
    else :
        askmethod() # recursive call if we dont find a match
    return

def selection(mylist):
    for i in range(len(mylist)) : 
        j=i
        for j in range(len(mylist)):
            temp = mylist[j]
            if temp > mylist[i]:
                mylist[j]=mylist[i]
                mylist[i]=temp
    return mylist

#def buble():
 #   for i in range(len(mylist)):
  #      if i+2 > len(mylist) :
   #         return mylist
    #    if mylist[i] > mylist[i+1]:
     #       mylist[i], mylist[i+1]= mylist[i+1], mylist[i]
    #return mylist
#i didnt did well the bublesort ill start over
# 
def buble(mylist):
    for i in range(len(mylist)):
        j=i+1
        for j in range(len(mylist)) :
            if mylist[j]<mylist[i]:
                mylist[j], mylist[i]= mylist[i], mylist[j]
            else : break
    return mylist    


askinput() 
