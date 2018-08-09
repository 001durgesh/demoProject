from sklearn import tree
#bumpy = 0, orange = 1
# smooth = 1, apple = 0
#Collect training
features = [ [150, 0], [170, 0], [140, 1], [130, 1],[145,1]]
labels = [ 1, 1, 0, 0,0]
#Train classifier
clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)
#Make Predictions
print clf.predict([[160, 0], [160, 1],[50,1]])