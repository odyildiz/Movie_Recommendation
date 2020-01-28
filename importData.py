from Movie import *
from User import *

item = open(r'C:\Users\ozgur\PycharmProjects\untitled1\u.item', 'r')  # Import movie data.

items = item.readlines()

userList = {}
movieList = {}


def importMovies():
    # Creating movie objects and set their id and title.
    for i in range(0, len(items)):
        tempItem = items[i].split("|")
        if tempItem[0] not in movieList:
            m = Movie()
            m.setId(int(tempItem[0]))
            m.setTitle(tempItem[1])
        movieList[m.getId()] = m
    return movieList


def importUsers(data):
    # Creating User objects and set their id, ratedMovies and rates.
    for i in data.iterrows():
        if data[0][i[0]] not in userList:
            u = User()
            u.setId(data[0][i[0]])
            u.addRatedMovies(data[1][i[0]], data[2][i[0]])
            userList[u.getId()] = u
        else:
            userList[data[0][i[0]]].addRatedMovies(data[1][i[0]], data[2][i[0]])
        movieList[data[1][i[0]]].addUsers(data[0][i[0]], data[2][i[0]])  # Add user's id and rating to movie that rated.
    return userList
