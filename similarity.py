import math

def mean(user):
    temp = 0
    for i in list(user.getRatedMovies().keys()):
        temp = temp + user.getRatedMovies()[i]
    return temp / len(list(user.getRatedMovies().keys()))

def pearson_correlation(user, userList, K):
    # user: current user.
    # userList: dictionary object that contain all users.
    # K: K number of kNN algorithm.

    similarityList = {}  # Dictionary that contain {"user": similarity} pair.
    response = {}  # Dictionary that contain kNN.
    for j in userList:
        if j == user.getId():
            continue
        temp1 = 0
        temp2 = 0
        temp3 = 0
        meanUser = mean(user)
        meanUser2 = mean(userList[j])
        for i in list(user.getRatedMovies().keys()):
            if i in list(userList[j].getRatedMovies().keys()):
                temp1 = temp1 + ((user.getRatedMovies()[i] - meanUser) * (userList[j].getRatedMovies()[i] - meanUser2))
                temp2 = temp2 + (user.getRatedMovies()[i] - meanUser) ** 2
                temp3 = temp3 + (userList[j].getRatedMovies()[i] - meanUser2) ** 2
        if temp2 * temp3 != 0:
            similarity = temp1 / math.sqrt(temp2 * temp3)
            similarityList[userList[j].getId()] = similarity
    sortedList = sorted(similarityList, key=similarityList.get, reverse=True)[:K]  # Sort by similarities and take kNN.
    for i in sortedList:
        response[i] = similarityList[i]
    return response

def cosine_similarity(user, askedItem, itemList, userList, K):
    # user: current user.
    # askedItem: movie that we want to make prediction.
    # itemList: dictionary object that contain all movies.
    # userList: dictionary object that contain all users.
    # K: K number of kNN algorithm.

    similarityList = {}  # Dictionary that contain {"item": similarity} pair.
    response = {}  # Dictionary that contain kNN.
    for j in itemList:
        if j == askedItem.getId():
            continue
        temp1 = 0
        temp2 = 0
        temp3 = 0
        for i in list(askedItem.getUsers().keys()):
            if i == user.getId():
                continue
            if i in list(itemList[j].getUsers().keys()):
                meanUser = mean(userList[i])
                temp1 = temp1 + (userList[i].getRatedMovies()[askedItem.getId()] - meanUser) * (
                        userList[i].getRatedMovies()[itemList[j].getId()] - meanUser)
                temp2 = temp2 + (userList[i].getRatedMovies()[askedItem.getId()] - meanUser) ** 2
                temp3 = temp3 + (userList[i].getRatedMovies()[itemList[j].getId()] - meanUser) ** 2
        if temp2 * temp3 != 0:
            similarity = temp1 / math.sqrt(temp2 * temp3)
            similarityList[itemList[j].getId()] = similarity
    sortedList = sorted(similarityList, key=similarityList.get, reverse=True)[:K]  # Sort by similarities and take kNN.
    for i in sortedList:
        response[i] = similarityList[i]
    return response