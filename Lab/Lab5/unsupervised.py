# -*- coding: utf-8 -*-
# Lab: Unsupervised Machine Learning. Clustering with sklearn
# CSCU9YE.  Gabriela Ochoa
# Characteristics of the IRIS dataset
# Features X:  sepal.length, sepal.width, petal.length, petal.width	
# Not using the target, instead explore clustering

from sklearn import datasets
import matplotlib.pyplot as plt

iris = datasets.load_iris() # load the dataset

# Print some information about the dataset
print("Feature names:", iris['feature_names'])
print("First five rows of data:\n", iris['data'][:5]) 


# Scatter plot with two selected variables
slength = iris.data[:,0]   # first column
swidth =  iris.data[:,1]    # 2nd column

plt.title('IRIS - No labels')
plt.xlabel('Sepal Length')
plt.ylabel('Sepal Width')
 # We are not using the targets for this excersize so, before clustering, all points are of the same color
plt.scatter(slength, swidth) 
plt.show()


# Creating a K-Means clustering algorithm
from sklearn.cluster import KMeans
km = KMeans(n_clusters = 3, random_state=0)
km.fit(iris.data)

# With the following code you can identify the center points of the data.
centers_km = km.cluster_centers_
print("Cluster Centres:")
print(centers_km)

# Compere the clustering with the "ground truth" (targets) using scatter plots
# First produce the scatter plot with real labels clustering

plt.figure()   # Creates a new window
plt.title('IRIS - Real Labels')
plt.xlabel('Speal Length')
plt.ylabel('Sepal Width')
plt.scatter(slength, swidth, c= iris.target)

# Now produce the plot with the labels produced by the clustering algorithm

plt.figure()   # Creates a new window
plt.title('IRIS - KM Cluster Labels')
plt.xlabel('Speal Length')
plt.ylabel('Sepal Width')
plt.scatter(slength, swidth, c= km.labels_)

# How do thay compare?

