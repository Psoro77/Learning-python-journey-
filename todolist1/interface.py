from tkinter import *
from taskmanager import Taskmanager
from tkcalendar import DateEntry
from datetime import datetime
from task import Task
class Interface:
    ##constructor for the interfaceshow the main page
    def __init__(self, manager :Taskmanager):
        self.manager= manager
        self.root= Tk()
        self.title = Label(self.root, text="TO DO LIST", font=("Helvetica", 18, "bold"), bg="#f0f0f0", fg="#333")
        self.title.pack(pady=10)
        self.root.geometry("600x400")  #mainframe
        self.root.configure(bg="#f0f0f0")
        self.button1 = Button(self.root, text="Add a Task", width=20, font=("Helvetica", 12), 
                              bg="#4CAF50", fg="white", command=self.createpanel)
        self.button1.pack(pady=5)

        # afficher les taches
        self.scrollbar = Scrollbar(self.root)
        self.scrollbar.pack(side=RIGHT, fill=Y)
        self.mylist = Listbox(self.root, yscrollcommand=self.scrollbar.set)
        self.mylist.pack(side=LEFT, fill=BOTH)
        self.scrollbar.config(command=self.mylist.yview) 
        self.showtask()
    def showtask(self):
        # Supprimer les anciens labels s'ils existent (pour éviter les doublons)
        self.mylist.delete(0, END)
        for task in self.manager.tasklist :
            name = task.getname()
            description = task.getdescription()
            date = task.getdate().strftime('%Y-%m-%d')
        #je dois mettre chacun d'entre un dans un label puis les pack
            self.mylist.insert(END, name + ':' + description + 'Due:' + date)   
        self.scrollbar.config(command=self.mylist.yview) 


        self.root.mainloop()



    ##page for the creation of a task
    def createpanel(self):
        self.creawindow = Toplevel(self.root)  # Meilleur que Tk() pour une 2e fenêtre
        self.creawindow.title("Add Task")
        Label(self.creawindow, text='task name' ).grid(row=0)
        Label(self.creawindow, text='Description' ).grid(row=1)
        e1 = Entry(self.creawindow)
        e2 = Entry(self.creawindow)
        e1.grid(row=0, column=1)
        e2.grid(row=1, column=1)

        Label(self.creawindow, text="Sélectionnez une date :").grid(row=2, column=0)
        self.cal = DateEntry(self.creawindow, date_pattern="dd/mm/yyyy")
        self.cal.grid(row=2, column =1)



        self.buttonclose = Button(self.creawindow, text='add a task', width ='25', command= lambda : self.createatask(e1, e2, self.cal) )
        self.buttonclose.grid(row=3, column=1, columnspan=2)
    #passing the data to the task manager object to create the task and put it in the list
    def createatask(self, name_entry, desc_entry, cal):
        self.date_obj = self.validate(cal)
        name = name_entry.get()
        description = desc_entry.get()

        if name and description:  # Vérifier que les champs ne sont pas vides
            self.manager.createtask(name, description, self.date_obj)
            self.creawindow.destroy()  # Fermer la fenêtre
            self.showtask()  # Mettre à jour l'affichage
        else:
            # Afficher un message d'erreur si les champs sont vides
            Label(self.creawindow, text="Please fill all fields", fg="red").grid(row=4, column=0, columnspan=2)



    def validate(self, cal):
       return  cal.get_date()  # Return a datetime.date


