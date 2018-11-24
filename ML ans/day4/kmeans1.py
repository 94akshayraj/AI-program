from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

x,y_true = make_blobs(n_samples = 300, centers = 4,  cluster_std=0.60)
kmeans = KMeans(n_clusters=4)
kmeans.fit(x)
y_kmeans = kmeans.predict(x)
plt.scatter(x[:,0], x[:,1], s = 50,c=y_kmeans,cmap='viridis')
plt.show()
