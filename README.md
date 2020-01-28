# Movie_Recommendation
User Based (Pearson Correlation) and Item Based (Adjusted Cosine Similarity) Movie Recommendation System

* This is the project that try to predict rating for a movie by using current user's previous ratings. Collaborative Filtering technique has used. 
* Project is working on console. 
* You need to add 5 movie for prediction.
* If you want to use evaluation, just take out tenfold() method in "test.py" from comment line.

**movieLens ml-100k data set has used as source.**

## Methods
**Evaluation:** k-fold Cross Validation and Mean Absolute Error(k=10)

**User Based Similarity:** Pearson Corellation Coefficient

**Item Based Similarity:** Adjusted Cosine Similarity

**Prediction:** k Nearest Neighbour has taken and used prediction formula.

