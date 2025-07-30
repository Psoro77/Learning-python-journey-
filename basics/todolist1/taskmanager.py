from task import Task
from typing import List
import sqlite3
from datetime import datetime
class Taskmanager :
    #contructor
    def __init__(self):
        self.tasklist: List[Task] =[]
        self.conn=sqlite3.connect('todolist.db')
        self.cur =self.conn.cursor()
        self.cur.execute("""
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                description TEXT,
                date TEXT,
                done INTEGER NOT NULL
            )
        """)
        self.conn.commit()
        for row in self.cur.execute("SELECT name, description, date, done FROM tasks"):
            name, desc, date_str, done_int = row
            date_obj = datetime.fromisoformat(date_str)

            self.createtask(name, desc, date_obj)
           # bool(done_int),


    # function to modify teh tasklist
    def createtask(self, name, description, date):

        date_str = date.isoformat()
        self.cur.execute(
            "INSERT INTO tasks (name, description, date, done) VALUES (?, ?, ?, 0)",
            (name, description, date_str)
        )
        self.conn.commit()

        ntask: Task = Task(name, description, date)
        self.addtolist(ntask)

    def addtolist(self, ntask):
        self.tasklist.append(ntask)

    def deletetolist(self, n : int):
        self.tasklist.pop(n)
        self.cur.execute("DELETE FROM tasks WHERE id = ?", (n,))
        self.conn.commit()
    #modify the task 
    def setdone(self, n: int):
        self.tasklist[n].donetask() 
        task = self.tasklist[n]
        self.cur.execute(
            "UPDATE tasks SET done = ? WHERE id = ?",
            (1 if task.done else 0, n)
        )
        self.conn.commit()

    #get the task
    def getask(self, n: int) -> Task:
        return self.tasklist[n]
    
    def close(self):
        self.conn.close()
    


