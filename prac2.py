import pandas as pd
import numpy as np
import pydotplus
from sklearn.externals.six import StringIO
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import export_graphviz

col_names = ['Age', 'Income', 'Gender', 'Martial_status', 'Buys']
col_names1 = ['Age', 'Income', 'Gender', 'Martial_status']
dataset = pd.read_csv('CosmeticShop.csv', header=None, names=col_names)
X = dataset.iloc[:,:-1]
Y = dataset.iloc[:,4]

le = LabelEncoder()
X = X.apply(le.fit_transform)
print(X)

model = DecisionTreeClassifier()
model.fit(X, Y)
X_in = np.array([2,2,1,0])
Y_pred = model.predict([X_in])
print("Prediction : "+Y_pred)

dot_data = StringIO()
export_graphviz(model, out_file=dot_data, filled=True,special_characters=True, feature_names=col_names1)
graph = pydotplus.graph_from_dot_data(dot_data.getvalue())
graph.write_png('ree1.png')