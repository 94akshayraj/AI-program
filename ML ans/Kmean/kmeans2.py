from sklearn.datasets import make_moons
from sklearn.cluster import KMeans
from sklearn.cluster import SpectralClustering
import matplotlib.pyplot as plt

X,y_true=make_moons(n_samples = 300, noise = 0.05)

kmeans = KMeans(n_clusters= 2)


model = SpectralClustering(2,affinity='nearest_neighbors')
labels = model.fit_predict(X)

plt.scatter(X[:,0],X[:,1],s=50,c=labels,cmap='viridis')
plt.show()
