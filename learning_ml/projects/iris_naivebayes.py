"""
Algoritmo de NaiveBayes para testar classificação no Iris Dataset

- Funciona bem para multiplas classes, não somente uma classificação de 2 ou 3 classes
- Funciona bem como uma classificação rápida
- Preciso de um dataset menor, mas não pode ser minusculo tb

! Todas as classificações precisam estar contidas no dataset
! Se as variáveis não forem independentes entre sí, o modelo não consegue performar bem

Beyond NB - SVM-NV (Classificação via SVM com características de NB, igual uma NN-Bayseana)

GaussianNB -> Melhor com dados continuos
BernoulliNB -> Melhor para dados binários
MultinomialNB -> Bernoulli para não-binários porém discretos
ComplementNB -> Multinomial para imbalanced datasets

"""

import os
import pandas as pd
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB

os.chdir('C:\\Users\\Antonio Coelho\\Codigos\\learning_ml\\projects\\iris')

dataset = pd.read_csv('iris.data', header=None, names=['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class'])

# Quando usamos values, pegamos somente o array ao invés do dataframe inteiro
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values

# Separamos treino e teste:
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

# Criamos o classificador:
classifier = GaussianNB()
# Treinamos o modelo com os dados
classifier.fit(X_train, y_train)
# Prevemos baseado no teste quanto que nosso modelo acerta
y_pred = classifier.predict(X_test)

# Reportamos os resultados do modelo:
print(classification_report(y_test, y_pred))
print(confusion_matrix(y_test, y_pred))

# Reportamos a acurácia do modelo:
print('Acurácia: ', accuracy_score(y_test, y_pred))
