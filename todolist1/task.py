import time

class Task:

    def __init__(self, name, description, date):
        self.name = name
        self.description =description
        self.date = date
        self.done = False

    #getters
    def getname(self) ->str:
        return self.name  
    def getdescription(self) ->str:
        return self.description
    def getdate(self) ->time:
        return self.name  
    def getprogress(self) ->bool :
        return self.done
    
    #mofiers
    def modifyname(self, name):
        self.name =name
    def modifydesc(self, description):
        self.description =description

    def modifydate(self, date):
        self.date = date

    def donetask(self) :
        self.done= True
    #tostring
    def __str__(self):
        return f"{self.name}({self.description})"

