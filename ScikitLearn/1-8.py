"""
保存我们的模型
"""

from sklearn.svm import SVC
from sklearn import datasets
import pickle
from sklearn.externals import joblib

data = datasets.load_iris()

X, Y = data.data, data.target

clf = SVC()
clf.fit(X, Y)

# method pickle
 
with open("./clf.pkl", "wb") as f:
  pickle.dump(clf, f)

# method joblib
# save
joblib.dump(clf, "./clf.pickle")
# restore
clf3 = joblib.load("./clf.pickle")