# -*- coding: utf-8 -*-
"""
Script para testar pre processing
"""

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

plt.style.use('ggplot')

# Lendo o dataset
df = pd.read_csv('http://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv ' , sep = ';')

# Tiramos a variável resultado, para testar o modelo
X = df.drop('quality' , 1).values
y1 = df['quality'].values

pd.DataFrame.hist(df, figsize = [15,15])

# Separamos para Y tudo o que for menor que 5
y = y1 <= 5

# plot histograms of original target variable
# and aggregated target variable
plt.figure(figsize=(20,5))
plt.subplot(1, 2, 1 )
plt.hist(y1);
plt.xlabel('original target value')
plt.ylabel('count')
plt.subplot(1, 2, 2)
plt.hist(y)
plt.xlabel('aggregated target value')
# plt.show()

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

from sklearn import neighbors, linear_model

knn = neighbors.KNeighborsClassifier(n_neighbors = 5)
knn_model_1 = knn.fit(X_train, y_train)

print('k-NN accuracy for test set: %f' % knn_model_1.score(X_test, y_test))

from sklearn.metrics import classification_report
y_true, y_pred = y_test, knn_model_1.predict(X_test)
print(classification_report(y_true, y_pred))

"""
Scaling & Centering - basic methods of preprocessing
"""

# Normalização - tornar o intervalo entre 0 e 1

# Standardization (Desvio padrão) -> (x-u)/z -> colocar a média em torno do 0 e tornar curva padrão

# Função scale faz standardization de todas as colunas numericas
from sklearn.preprocessing import scale
Xs = scale(X)
Xs_train, Xs_test, y_train, y_test = train_test_split(Xs, y, test_size=0.2, random_state=42)
knn_model_2 = knn.fit(Xs_train, y_train)
print('k-NN score for test set: %f' % knn_model_2.score(Xs_test, y_test))
print('k-NN score for training set: %f' % knn_model_2.score(Xs_train, y_train))
y_true, y_pred = y_test, knn_model_2.predict(Xs_test)
print(classification_report(y_true, y_pred))
