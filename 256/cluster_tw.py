import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import AgglomerativeClustering

# data
a, b, c, d = (4, 10), (7, 10), (4,8), (6,8)
x, y, z=(3,4), (2,2), (5,2)
l, m, n, o, k=(12,6), (9,3), (12,3), (11,4), (11,4), (10,5)
data = np.array([a,b,c,d,x,y,z,l,m,n,o,k])

data = np.array([(2,6),(3,7),(5,8),(5,5),(6,6),(2,2),(5,2),(7,3),(8,4),(10,6),(12,8)])  

# single link
single_link_cluster = AgglomerativeClustering(n_clusters=5, linkage='single').fit(data)
plt.figure(figsize=(5,5))
plt.scatter(data[:,0], data[:,1], c=single_link_cluster.labels_, cmap='rainbow')
plt.show()
# complete link
complete_link_cluster = AgglomerativeClustering(n_clusters=5, linkage='complete').fit(data)
plt.figure(figsize=(5,5))
plt.scatter(data[:,0], data[:,1], c=complete_link_cluster.labels_, cmap='rainbow')
plt.show()
# average link
avg_link_cluster = AgglomerativeClustering(n_clusters=5, linkage='average').fit(data)
plt.figure(figsize=(5,5))
plt.scatter(data[:,0], data[:,1], c=avg_link_cluster.labels_, cmap='rainbow')
plt.show()













