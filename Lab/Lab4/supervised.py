# -*- coding: utf-8 -*-
# Lab: Supervised Machine Learning. Classification with sklearn
# CSCU9YE.  Gabriela Ochoa
# Characteristics of the IRIS dataset
# Features X:  sepal.length, sepal.width, petal.length, petal.width	
# Target  y :  Flower variety

from sklearn import datasets
import matplotlib.pyplot as plt

iris = datasets.load_iris() # load the dataset

# Print some information about the dataset
print("Dataset Dimensions: ", iris.data.shape)   
print("Target names:", iris['target_names']) 
print("Feature names:", iris['feature_names'])
print("Long Description of dataset:", iris['DESCR']) 
print("First five rows of data:\n", iris['data'][:5]) 


# Scatter plot with two selected variables
slength = iris.data[:,0]   # first column
swidth =  iris.data[:,1]    # 2nd column
plt.title('Scatter plot IRIS')
plt.xlabel('sepal length')
plt.ylabel('sepal width')
plt.scatter(slength, swidth, c=iris.target)  # the color of the dot is given by the class of flower
plt.show()


# Scatter plot with two selected variables
swidth = iris.data[:,1]   # first column
pwidth = iris.data[:,3]    # 2nd column
plt.figure()
plt.title('Scatter plot IRIS')
plt.xlabel('sepal width')
plt.ylabel('petal width')
plt.scatter(swidth, pwidth, c=iris.target)  # the color of the dot is given by the class of flower
plt.show()




# Creating training and testing set
from sklearn.model_selection import train_test_split
#from sklearn.cross_validation import train_test_split # Depending on version of sklearn

X_train, X_test, y_train, y_test = train_test_split(iris['data'], iris['target'], random_state=0)

# Print size of training set
print("X_train shape:", X_train.shape)
print("y_train shape:", y_train.shape)

# Print size of test set
print("X_test shape:", X_test.shape)
print("y_test shape:", y_test.shape)

# Building our first model: k-Nearest Neighbor
from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, y_train)


# Making Predictions of a new flower, where we have the measurament
import numpy as np
X_new = np.array([[5, 2.9, 1, 0.2]])
print("X_new.shape:", X_new.shape)

prediction = knn.predict(X_new)

print("Prediction:", prediction)
print("Predicted target name:",
       iris['target_names'][prediction])
       
# Evaluating the model - Computing the Accuracy or Score
# Accuracy measures the proportion of correct predictions, that is
# the proportion of times the predicted value is the same than the real (observed value)

y_pred = knn.predict(X_test)

print("Test set predictions:\n", y_pred)
print("Test set score: {:.2f}".format(np.mean(y_pred == y_test)))
print("Test set score: {:.2f}".format(knn.score(X_test, y_test)))
       

