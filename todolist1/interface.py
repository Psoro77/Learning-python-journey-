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
        self.title = Label(self.root, text='TO DO LIST')
        self.title.pack() 
        self.button1 = Button(self.root, text='add a task', width ='25', command= self.createpanel )
        self.button1.pack()

        # afficher les taches
        self.showtask()
    def showtask(self):
        # Supprimer les anciens labels s'ils existent (pour éviter les doublons)
        for widget in self.root.winfo_children():
            if isinstance(widget, Label) and widget != self.title:
                widget.destroy()
        for task in self.manager.tasklist :
            name = task.getname()
            description = task.getdescription()
            date = task.getdate().strftime('%Y-%m-%d')
        #je dois mettre chacun d'entre un dans un label puis les pack
            task_text = f"{name}: {description} (Due: {date})"
            task_label = Label(self.root, text=task_text)
            task_label.pack()



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


