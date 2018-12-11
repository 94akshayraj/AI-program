from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from mpl_toolkits import mplot3d

data = pd.read_csv("/Users/spacslug/ML-Day1/ML ans/day4/data_breast.txt", delim_whitespace = True)

data = data.as_matrix()

f1=data[:,0]
f2=data[:,1]
f3=data[:,2]
X=np.array(zip(f1,f2,f3))
print(X)

kmeans=KMeans(n_clusters=5)
kmeans.fit(X)
y_kmeans=kmeans.predict(X)

fig = plt.figure()
ax=plt.axes(projection='3d')
ax.scatter3D(f1,f2,f3,c=y_kmeans,cmap='viridis')

plt.show()

centers=kmeans.cluster_centers_

plt.scatter(X[:,0],X[:,1],s=50,c=y_kmeans,cmap='viridis')
plt.scatter(centers[:,0],centers[:,1],s=200,c='red')
plt.show()
