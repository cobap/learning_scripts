import os
import pandas as pd
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn import linear_model


os.chdir('C:\\Users\\Antonio Coelho\\Codigos\\learning_ml\\projects\\iris')

dataset = pd.read_csv('iris.data', header=None, names=['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class'])

dataset.columns

# Entendendo como as classes se distribuem conforme a variável independente
sns.catplot(x='class', y='sepal_length', kind='swarm', data=dataset)
sns.catplot(x='class', y='sepal_width', kind='swarm', data=dataset)
sns.catplot(x='class', y='petal_length', kind='swarm', data=dataset)
sns.catplot(x='class', y='petal_width', kind='swarm', data=dataset)

# Entendendo relacionamento entre length e width para cada classe
sns.relplot(x='sepal_length', y='sepal_width', hue='class', kind='scatter', data=dataset)
sns.relplot(x='petal_length', y='petal_width', hue='class', kind='scatter', data=dataset)
sns.relplot(x='petal_length', y='sepal_length', hue='class', kind='scatter', data=dataset)
sns.relplot(x='petal_width', y='sepal_width', hue='class', kind='scatter', data=dataset)
sns.relplot(x='petal_width', y='sepal_length', hue='class', kind='scatter', data=dataset)
sns.relplot(x='sepal_width', y='petal_length', hue='class', kind='scatter', data=dataset)

# Pelos gráficos podemos perceber que setosa é fácilmente linearmente separável das outras duas petalas
# Em contrapartida, virginica e versicolor são mais difíceis para detectar a diferença, mas ainda conseguem ser linearmente
# separáveis com grande acurácia

# Vamos separar entre teste e treino
# Fazendo desse modo é prático mas não temos a separação entre X e y
train, test = train_test_split(dataset, test_size=0.3, random_state=42)

# REVIEW AQUI - PQ ISSO NAO FUNCIONA?
X_train, X_test, y_train, y_test = train_test_split(X=dataset.iloc[:, 0:4].to_numpy(), y=dataset.iloc[:, 4].to_numpy(), test_size=0.3, random_state=42)

regressao1 = linear_model.LinearRegression()

regressao1.fit()
