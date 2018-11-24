from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier

#import sklearn
iris = load_iris()
X = iris.data
y = iris.target

knn = KNeighborsClassifier (n_neighbors = 1)
knn.fit(X,y)
p=knn.predict([[3,5,4,2]])
print p
