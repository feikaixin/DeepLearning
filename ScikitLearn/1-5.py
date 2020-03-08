"""
交叉验证  cross_val_score 
"""

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import cross_val_score


iris = load_iris()
X = iris.data
Y = iris.target


knn_model = KNeighborsClassifier(n_neighbors=5)

scores = cross_val_score(knn_model, X, Y, scoring="accuracy", cv=5)

print(scores.mean())