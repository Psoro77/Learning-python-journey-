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
        self.task_canvas = Canvas(self.root, bg="#f0f0f0", highlightthickness=0)
        self.task_scrollbar = Scrollbar(self.root, orient=VERTICAL, command=self.task_canvas.yview)
        self.task_frame = Frame(self.task_canvas, bg="#f0f0f0")
        
        self.task_canvas.configure(yscrollcommand=self.task_scrollbar.set)
        self.task_scrollbar.pack(side=RIGHT, fill=Y)
        self.task_canvas.pack(side=LEFT, fill=BOTH, expand=True, padx=10, pady=10)
        
        self.task_canvas.create_window((0, 0), window=self.task_frame, anchor="nw")
        self.task_frame.bind("<Configure>", lambda e: self.task_canvas.configure(scrollregion=self.task_canvas.bbox("all")))

        # Afficher les tâches
        self.showtask()

        self.root.mainloop()


    def showtask(self):
        # Supprimer les anciens widgets dans task_frame
        for widget in self.task_frame.winfo_children():
            widget.destroy()

        # Afficher chaque tâche
        for idx, task in enumerate(self.manager.tasklist):
            # Créer un cadre pour chaque tâche
            task_frame = Frame(self.task_frame, bg="white", bd=1, relief=SOLID)
            task_frame.pack(fill=X, padx=5, pady=5)

            # Nom de la tâche
            name = task.getname()
            description = task.getdescription()
            date_obj = task.getdate()
            
            # Vérifier que date_obj est valide
            date_str = date_obj.strftime('%Y-%m-%d') 
            
            # Statut de la tâche
            status = "Done" if task.getprogress() else "Pending"
            status_color = "green" if task.getprogress() else "red"

            # Afficher les informations
            Label(task_frame, text=f"Task: {name}", font=("Helvetica", 12, "bold"), bg="white").pack(anchor="w", padx=5, pady=2)
            Label(task_frame, text=f"Description: {description}", font=("Helvetica", 10), bg="white").pack(anchor="w", padx=5)
            Label(task_frame, text=f"Due: {date_str}", font=("Helvetica", 10), bg="white").pack(anchor="w", padx=5)
            Label(task_frame, text=f"Status: {status}", font=("Helvetica", 10), fg=status_color, bg="white").pack(anchor="w", padx=5)

            # Boutons d'action
            button_frame = Frame(task_frame, bg="white")
            button_frame.pack(anchor="e", padx=5, pady=5)
            if task.getprogress() :
                Button(button_frame, text="Ongoing", width=8, bg="#f44336", fg="white", 
                    command=lambda i=idx: self.donema(i)).pack(side=LEFT, padx=2)
            else :
                Button(button_frame, text="Done", width=8, bg="#4CAF50", fg="white", 
                    command=lambda i=idx: self.donema(i)).pack(side=LEFT, padx=2)
            Button(button_frame, text="Delete", width=8, bg="#f44336", fg="white", 
                   command=lambda i=idx: self.deletema(i)).pack(side=LEFT, padx=2)
            
        
    def deletema(self, n):
        self.manager.deletetolist(n)
        self.showtask()
    def donema(self, n):
        self.manager.setdone(n)
        self.showtask()
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


