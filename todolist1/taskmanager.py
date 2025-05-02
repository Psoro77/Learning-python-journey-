from task import Task
from typing import List

class taskmanager :

    def __init__(self):
        self.tasklist: List[Task] =[]

    def createtask(self, name, description, date):
        ntask: Task = Task(name, description, date)
        self.addtolist(ntask)
    def addtolist(self, ntask):
        self.tasklist.append(ntask)
    def deletetolist(self, n : int):
        self.tasklist.pop(n)
        
