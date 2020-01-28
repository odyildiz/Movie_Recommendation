from importData import *
from evaluation import tenfold
from prediction import *
from User import *
import pandas as pd

data = pd.read_csv(r'C:\Users\ozgur\PycharmProjects\untitled1\u.data', sep="\t", header=None)  # Importing u.data file into DataFrame object.

# tenfold(data)
# For evaluation you can use tenfold method. Just take out upper line from comment. Evaluation can take long time.
# If you have suggestion for improving evaluation part please suggest me :)

movieList = importMovies()  # Dictionary object that contain all movie objects.
userList = importUsers(data)  # Dictionary object that contain all user objects.

u = User()
while len(u.getRatedMovies()) < 5:
    for j in movieList:
        print(movieList[j].getId(), " - ", movieList[j].getTitle())
    print("Please rate at least 5 movie. Remaining : ", 5-len(u.getRatedMovies()))
    movieAdd = int(input("Choose a Movie"))
    if movieAdd > 1682 or movieAdd < 0:
        print("There is no item like that.")
        continue
    rating = int(input("What is your Rating"))
    if rating > 5 or rating < 0:
        print("Out of bound. Try Again!!")
        continue
    u.addRatedMovies(movieAdd, rating)

moviePred = int(input("Choose a movie for prediction"))

print("Cosine Prediction  for -> ", movieList[moviePred].getId(), " - ", movieList[moviePred].getTitle())
print(cosine_prediction(userList[2], userList, movieList, 80, movieList[moviePred]))

print("Pearson Prediction  for -> ", movieList[moviePred].getId(), " - ", movieList[moviePred].getTitle())
print(pearson_prediction(userList[2], userList, 80, movieList[moviePred]))

