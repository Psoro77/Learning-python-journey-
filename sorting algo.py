#in this file i am going to try to create some sorting algorith by my own to understant more array in python
#and loops and keys ect so im going to create some function and just ask the user for a method to use and also for some 
#input
import sys
mylist = []
def askinput ():
    print('please enter some number enter s To stop the input')
    inp = input()
    if inp == "s":
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
        sys.exit
    elif 'Selection'in meth:
        selection()
    elif 'Buble'in meth:
        buble()
    elif 'insertion'in meth:
        insertion()
    elif 'quick'in meth:
        quick()
    else :
        askmethod() # recursive call if we dont find a match
askinput() 
