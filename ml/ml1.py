import sklearn
from sklearn import tree
# Training Data...

features = [ [130,1], [140,1], [150,0], [170,0]]
label = [0,0,1,1]

# Train Classifier...

clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, label)

# Make Predictions...

print clf.predict([[150,0]])