class Name ():
    totalNames = 0

    def __init__(self, name, id):
        self.name = name
        self.id = id

    def __str__(self):
        return "{ id : " + str(self.id) + " name : " + self.name + " }"

    # nameDict = ['', '', '', '', '', '', '', '', '', '']
