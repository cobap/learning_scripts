import os
import graphviz
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import tree
from sklearn.tree.export import export_text
from sklearn.model_selection import train_test_split

os.chdir('C:\\Users\\Antonio Coelho\\Codigos\\learning_ml\\projects\\iris')


dataset = pd.read_csv('iris.data', header=None, names=['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class'])
train, test = train_test_split(dataset, test_size=0.3, random_state=42)

clf = tree.DecisionTreeClassifier()
clf = clf.fit(train.iloc[:, :4].to_numpy(), train.iloc[:, -1].to_numpy())
tree.plot_tree(clf, ax=plt.subplots(figsize=(10, 10))[1], class_names=list(set(train.iloc[:, -1].values)), feature_names=list(train.iloc[:, :4].columns))



# text_answer = export_text(clf, feature_names=list(train.iloc[:, :4].columns))
# print(text_answer)



# clf_regression = tree.DecisionTreeRegressor()
# clf_regression = clf_regression.fit(train.iloc[:, :4].to_numpy(), train.iloc[:, -1].to_numpy())
# tree.plot_tree(clf_regression, ax=plt.subplots(figsize=(10, 10))[1])
