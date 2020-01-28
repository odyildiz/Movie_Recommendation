class User:
    def __init__(self):
        self.name = ''
        self.id = 0
        self.password = ""
        self.ratedMovies = {}

    def getName(self):
        return self.name
    def setName(self, value):
        self.name = value
    def getId(self):
        return self.id
    def setId(self, value):
        self.id = value
    def getPassword(self):
        return self.password
    def setPassword(self, value):
        self.password = value
    def getRatedMovies(self):
        return self.ratedMovies
    def addRatedMovies(self, key, value):
        self.ratedMovies[key] = value