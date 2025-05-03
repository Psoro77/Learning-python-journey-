from task import Task
from typing import List

class Taskmanager :
    #contructor
    def __init__(self):
        self.tasklist: List[Task] =[]


    # function to modify teh tasklist
    def createtask(self, name, description, date):
        ntask: Task = Task(name, description, date)
        self.addtolist(ntask)
    def addtolist(self, ntask):
        self.tasklist.append(ntask)
    def deletetolist(self, n : int):
        self.tasklist.pop(n)
    #modify the task 
    def setdone(self, n: int):
        self.tasklist[n].donetask() 


    #get the task
    def getask(self, n: int) -> Task:
        return self.tasklist[n]
    


