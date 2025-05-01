class task:



    def __init__(self, name, description, date):
        self.name = name
        self.description =description
        self.date = date

    def modifyname(self, name):
        self.name =name


    def __str__(self):
        return f"{self.name}({self.description})"