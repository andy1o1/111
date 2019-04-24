import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

df = pd.DataFrame({'X': [0.1, 0.15, 0.08, 0.16, 0.2, 0.25, 0.24, 0.3],
                   'y': [0.6, 0.71, 0.9,  0.85, 0.3, 0.5,  0.1,  0.2]})
f1 = df['X'].values
f2 = df['y'].values
X = np.array(list(zip(f1, f2)))  # {[0.1,0.6],...}
print("Initial pairs : ", X)

C_x = np.array([0.1, 0.3])
C_y = np.array([0.6, 0.2])
centroid = C_x, C_y

plt.scatter(f1, f2, color="#ff0000")
plt.scatter(C_x[0], C_y[0], color="b", marker='*', s=200)
plt.scatter(C_x[1], C_y[1], color="b", marker='*', s=200)
plt.show()

#model = KMeans(n_clusters=2, init=np.array([[0.1, 0.6], [0.3, 0.2]]))
model=KMeans(n_clusters=2, random_state=0)
model.fit(X)
labels = model.labels_
print("Labels are: ", labels)
count = 0
for i in range(len(labels)):
    if (labels[i] == 1):
        count = count + 1
        
print("P6 balongs to cluster",model.labels_[5])
# elems, count = np.unique(labels, return_count = True)

print("Number of points around cluster 2 is : ", count)
newcentroids = model.cluster_centers_
print("Old centroids are  :", centroid[0], " ", centroid[1])
print("New centroids are  :", newcentroids[0], " ", newcentroids[1])
C1_x = np.array([newcentroids[0]])
C1_y = np.array([newcentroids[1]])
print(C1_x, C1_y)
plt.scatter(f1, f2, color="#ff0000")
plt.scatter(C1_x[0], C1_y[0], color="b", marker='*', s=200)
# plt.scatter(C1_x[1],C1_y[1],color="b", marker='*',s=200)
plt.show()
