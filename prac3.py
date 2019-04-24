import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsClassifier

dataset = pd.read_csv('KNNPoints.csv')
X = dataset.iloc[:,:-1].values
Y = dataset.iloc[:,2].values

classifier = KNeighborsClassifier(n_neighbors=3)
classifier.fit(X,Y)
X_test = np.array([6,6])
Y_pred = classifier.predict([X_test])
print("Output : ",Y_pred)