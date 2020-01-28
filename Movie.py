class Movie:
    def __init__(self):
        self.title = ''
        self.id = 0
        self.users = {}

    def getTitle(self):
        return self.title
    def setTitle(self, value):
        self.title = value
    def getId(self):
        return self.id
    def setId(self, value):
        self.id = value
    def getUsers(self):
        return self.users
    def addUsers(self, key, value):
        self.users[key] = value