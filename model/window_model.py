
class windowModel:

    def __init__(self):
        super().__init__()


    def uploadToDB(self, text):
        with open('notes.txt', 'w') as f:
            f.write(text)

    def readDB(self):
        f = open("notes.txt", "r")
        if f.mode == 'r':
            database = f.readlines()
            return database

