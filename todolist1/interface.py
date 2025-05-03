from tkinter import *
from taskmanager import Taskmanager
class Interface:
    def __init__(self, manager :Taskmanager):
        self.manager= manager
        self.root= Tk()
        self.title = Label(self.root, text='TO DO LIST')
        self.title.pack() 
        self.button1 = Button(self.root, text='add a task', width ='25', command= self.createpanel() )
        self.button1.pack
        self.root.mainloop()




    def createpanel(self):
        creawindow = Toplevel(self.root)  # Meilleur que Tk() pour une 2e fenêtre
        creawindow.title("Add Task")
        Label(creawindow, text='task name' ).grid(row=0)
        Label(creawindow, text='Description' ).grid(row=1)
        e1 = Entry(creawindow)
        e2 = Entry(creawindow)
        e1.grid(row=0, column=1)
        e2.grid(row=1, column=1)

        buttonclose = creawindow.Button(creawindow, text='add a task', width ='25', command= creawindow.destroy,  )
        buttonclose.pack
        creawindow.mainloop()



