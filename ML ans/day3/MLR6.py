from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import cross_val_score

#import sklearn
iris = load_iris()
X = iris.data
y = iris.target

knn = KNeighborsClassifier (n_neighbors = 1)

score = cross_val_score(knn,X,y,cv=10)
print(score)