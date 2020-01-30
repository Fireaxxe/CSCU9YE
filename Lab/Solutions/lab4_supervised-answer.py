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

# Creating training and testing set
from sklearn.model_selection import train_test_split
from sklearn import metrics #Import scikit-learn metrics module for accuracy calculation


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
knn = knn.fit(X_train, y_train)


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

knn_y_pred = knn.predict(X_test)


print("KNN Test set predictions:\n", knn_y_pred)
       
# Model Accuracy, how often is the classifier correct?
print("KNN Accuracy: ", metrics.accuracy_score(y_test, knn_y_pred)) # formatting to only two decimals
print("KNN Accuracy:  {:.2f}".format(metrics.accuracy_score(y_test, knn_y_pred))) # formatting to only two decimals


# Create Decision Tree classifer object
from sklearn.tree import DecisionTreeClassifier 
dtree = DecisionTreeClassifier()

# Train Decision Tree Classifer
dtree = dtree.fit(X_train,y_train)

#Predict the response for test dataset
dtree_y_pred = dtree.predict(X_test)

# Making Predictions of example above
prediction = dtree.predict(X_new)

print("Decision Tree Prediction:", prediction)
print("Predicted target name:",
       iris['target_names'][prediction])
       
# Evaluating the model - Computing the Accuracy or Score
# Accuracy measures the proportion of correct predictions, that is
# the proportion of times the predicted value is the same than the real (observed value)

dtree_y_pred = dtree.predict(X_test)

print("Decision Tree Test set predictions:\n", dtree_y_pred)
       
# Model Accuracy, how often is the classifier correct?
print("Decision Tree Accuracy: ", metrics.accuracy_score(y_test, dtree_y_pred)) # formatting to only two decimals
print("Decision TreeAccuracy:  {:.2f}".format(metrics.accuracy_score(y_test, dtree_y_pred))) # formatting to only two decimals


