from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score,confusion_matrix
import pandas as pd
import matplotlib.pyplot as plt

wart = pd.read_csv("/home/ai3/Desktop/common/ML/Day2/Questions/Immunotherapy.csv")
warts = wart.as_matrix()

X = warts[:,0:6]
y = warts[:,7]



X_train,X_test,y_train,y_test = train_test_split(X,y,test_size = 0.2)


scores = []
for i in range(1,25):
	knn = KNeighborsClassifier (n_neighbors = i)
	knn.fit(X_train,y_train)
	p = knn.predict(X_test)
	
	confusion_matrix(y_test,p)
	a = accuracy_score(y_test,p)
	scores.append(a)
#print score
plt.plot(range(1,25),scores)
plt.show()