from importData import *
from prediction import *

def tenfold(data):

    length = len(data)
    movieList = importMovies()
    meanAbsErrorP = 0
    meanAbsErrorC = 0

    for i in range(0, 10):
        dividerP = 0
        dividerC = 0
        errorP = 0
        errorC = 0

        startIndex = int((i / 10) * length)  # Finding where to start splitting for test set.
        stopIndex = int(((i+1) / 10) * length)  # Finding where to stop splitting for test set.
        veri = data.copy()
        Testing = veri[startIndex:stopIndex]  # Splitting data into test set.
        pearsonTest = Testing.sort_values(by=[0]).set_index([list(range(startIndex, stopIndex))])  # Sorting Testing data by userId for faster prediction.
        cosineTest = Testing.sort_values(by=[1]).set_index([list(range(startIndex, stopIndex))])  # Sorting Testing data by movieId for faster prediction.
        Training = veri.drop(veri.index[startIndex:stopIndex])  # Splitting data into training set.

        userList = importUsers(Training)  # Dictionary object that contain all user objects.

        for j in range(startIndex,stopIndex):
            pearson = pearson_prediction(userList[pearsonTest[0][j]], userList, 10, movieList[pearsonTest[1][j]])
            cosine = cosine_prediction(userList[cosineTest[0][j]], userList, movieList, 10, movieList[cosineTest[1][j]])
            if pearson is not None:
                dividerP = dividerP + 1
                errorP = errorP + abs(pearson - Testing[2][j])
            if cosine is not None:
                dividerC = dividerC + 1
                errorC = errorC + abs(cosine - Testing[2][j])

        meanAbsErrorP = meanAbsErrorP + (errorP/dividerP)
        meanAbsErrorC = meanAbsErrorC + (errorC/dividerC)
        print("PearsonError ->", meanAbsErrorP, " -meanErrors- Iteration", i+1, " CosineError -> ", meanAbsErrorC)

    print("Mean Absoluter Error for Pearson -> ", meanAbsErrorP/10)
    print("Mean Absoluter Error for Cosine -> ", meanAbsErrorC/10)
