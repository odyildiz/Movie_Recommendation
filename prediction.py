from similarity import *

class pred:
    prevUser = None  # Previous user that was predicted.
    pearsonSim = {}  # Previous user's similarity.

    prevItem = None  # Previous item that was predicted.
    cosineSim = {}  # Previous item's similarity.

def pearson_prediction(user, userList, K, askedItem):
    # user: current user.
    # userList: dictionary object that contain all users.
    # K: K number of kNN algorithm.
    # askedItem: movie that we want to make prediction.

    if user != pred.prevUser:  # This part is made for decreasing time evaluation. If current and previous user is same we dont need to calculate similarity again.
        pred.prevUser = user  # If current user is different from previous one we assign current user to prevUser.
        pred.pearsonSim = pearson_correlation(user, userList, K)  # If current user is different from previous one we assign current user's similarity list to pearsonSim.
    temp1 = 0
    temp2 = 0

    meanUser = mean(user)
    for i in pred.pearsonSim:
        meanUser2 = mean(userList[i])
        '''''
        # If a movie that we want to predict is not in any of best K neighbour's ratedMovies list, we try to predict 
        # that movie for that neighbour for only one time. It can improve accuracy but increase computing time.
        # For use this, just take this part out of comment. 
        
        if askedItem.getId() not in userList[i].getRatedMovies():
            newSim = pearson_correlation(userList[i], userList, K)
            temp3 = 0
            temp4 = 0
            for j in newSim:
                meanUser3 = mean(userList[j])
                if askedItem.getId() not in userList[j].getRatedMovies():
                    continue
                temp3 = temp3 + newSim[j]*(userList[j].getRatedMovies()[askedItem.getId()] - meanUser3)
                temp4 = temp4 + newSim[j]
            if temp4 != 0:
                newPred = meanUser2 + temp3/temp4
                userList[i].addRatedMovies(askedItem.getId(), newPred)
        '''''
        if askedItem.getId() not in userList[i].getRatedMovies():
            continue
        temp1 = pred.pearsonSim[i]*(userList[i].getRatedMovies()[askedItem.getId()] - meanUser2) + temp1
        temp2 = pred.pearsonSim[i] + temp2
    if temp2 == 0:
        return None
    else:
        prediction = meanUser + temp1/temp2
        return round(prediction)

def cosine_prediction(user, userList, itemList, K, askedItem):
    # user: current user.
    # userList: dictionary object that contain all users.
    # itemList: dictionary object that contain all movies.
    # K: K number of kNN algorithm.
    # askedItem: movie that we want to make prediction.

    if askedItem != pred.prevItem:  # This part is made for decreasing time evaluation. If current and previous item is same we dont need to calculate similarity again.
        pred.prevItem = askedItem  # If current item is different from previous one we assign current item to prevItem.
        pred.cosineSim = cosine_similarity(user, askedItem, itemList, userList, K)  # If current item is different from previous one we assign current item's similarity list to cosineSim.
    temp1 = 0
    temp2 = 0
    for i in pred.cosineSim:
        '''''
        # If a movie that we want to predict is not in current user's ratedMovies list, we try to predict 
        # that movie for that user for only one time. It can improve accuracy but increase computing time.
        # For use this, just take this part out of comment. 
        
        if i not in user.getRatedMovies():
            newSim = cosine_similarity(user, itemList[i], itemList, userList, K)
            temp3 = 0
            temp4 = 0
            for j in newSim:
                if j not in list(user.getRatedMovies().keys()):
                    continue
                temp3 = temp3 + newSim[j]*user.getRatedMovies()[j]
                temp4 = temp4 + newSim[j]
            if temp4 != 0:
                newPred = temp3/temp4
                user.addRatedMovies(j, newPred)
        '''''
        if i not in user.getRatedMovies():
            continue
        temp1 = temp1 + pred.cosineSim[i]*user.getRatedMovies()[i]
        temp2 = temp2 + pred.cosineSim[i]
    if temp2 == 0:
        return None
    else:
        prediction = temp1/temp2
        return round(prediction)