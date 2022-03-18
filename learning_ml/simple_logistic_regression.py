import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix
import math

"""
Exemplo Rede neural simples
"""
# Teste rápido de dimensoes
inputs = np.array([0.1, 0.5, 1.1, 2.3, -1.1, -2.3, -1.5, -2.5])
inputs = inputs.reshape(4,2)

weights = np.array([0.1, 0.2, 0.3, 0.1, 0.2, 0.3])
weights = weights.reshape(2,3)

bias = np.array([0.01, 0.1, 0.1])
bias = bias.reshape(-1, 3)

ones = np.ones(4).reshape(4,-1)
inputs_biased = np.append(ones, inputs, axis=1)

weights_biased = np.append(bias, weights, axis=0)

z_matrix = inputs_biased @ weights_biased

"""
Agora calculamos softmax da rede
"""
softmax_result = np.exp(z_matrix) / np.sum(np.exp(z_matrix), axis=1).reshape(-1, 1)
# Voltamos os resultados para classes
softmax_result.argmax(axis=1)

# Calcula Cross-Entropies
expected_y = np.array([0,1,2,2])
softmax_result

# Depois rever como podemos calcular isso de maneira efetiva
np.array(
[math.log(0.294506) * 1 + math.log(0.21) * 0 + math.log(0.42) * 0,
math.log(0.29) * 0 + math.log(0.327228) * 1 + math.log(0.42) * 0,
math.log(0.29) * 0 + math.log(0.21) * 0 + math.log(0.237589) * 1,
math.log(0.29) * 0 + math.log(0.21) * 0 + math.log(0.220954) * 1])

# Aqui terminamos, depois só tirar a derivada e reajustar os pesos da rede

"""
###############
REGRESSÃO LOGISTICA COM SKLEARN
###############
"""


# Fake data just to test
# We reshape X so it has 2 dimensions, like a "imaginary" table. Which index 0 represents the whole table, and every index i is a column
# When we use -1, we dont know the length of rows to be compatible with, so we draw first the columns, and then define the rows
x = np.arange(10).reshape(-1, 1)
# Array é bidimensional, sendo 10 linhas e 1 coluna
print(x.shape)
y = np.array([0, 0, 0, 0, 1, 1, 1, 1, 1, 1])

# Agora criamos o modelo
# Penalty L2 as default, but we can change it to L1 if we want to
penalty = 'l1'
model = LogisticRegression(solver='liblinear', random_state=0, penalty=penalty)

# LibLinear does not work without regularization
# Other solvers do not support L1 regularization
# Saga solver is the only one that supports ElasticNet regularization

# We not fit the data into the model
model.fit(x, y)

# To get how the model divided the classes
model.classes_
model.intercept_


# To evaluate the model, we see how he would predict every number in our 10length array
model.predict_proba(x)

# To get the real prediction:
model.predict(x)

# Recuperando o score do modelo
model.score(x, y)

# Mas temos que rodar a matrix de confusão visto que esses resultados podem ser falso positivos ou falso negativos
confusion_matrix(y, model.predict(x))
# Formato da matrix:
# [True N   False P]
# [False N  True P]

# To get a more extensive report, we can use classification report
print(classification_report(y, model.predict(x)))

"""
VERIFICANDO HANDWRITE DIGITS COM REGRESSÃO LOGISTICA
"""
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

x, y = load_digits(return_X_y=True)

# Para ver qual o valor do numero e o correspondente numero
# Primeira imagem
plt.imshow(x[35].reshape(8,8))
y[35]

# Muito importante dividir os dados entre treino e teste
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=0)

# Muito importante padronizar os dados
# Padronizar significa transformar os dados até que a média de cada coluna seja 0, e o desvio padrão seja 1. Ou seja, transformar a distribuição dos dados em uma N(0,1)

# Para padronizar, calculamos média e desvio-padrão para cada coluna (feature)
# Subtraimos a média de cada elemento, como se fossemos calcular a variancia
# Ao invés de dividir por N, dividimos pelo desvio-padrão da amostra
# StandardScaler faz esse trabalho para gente
scaler = StandardScaler()
x_train = scaler.fit_transform(x_train)

# Agora criamos o modelo novamente
# Como nesse caso temos até 9 classes distintas devido aos numeros, devemos informar o parametro multi_class. Ovr diz para considerar binario (ou é ou não é daquela classe)
model = LogisticRegression(solver='liblinear', C=0.05, multi_class='ovr', random_state=0).fit(x_train, y_train)

# Para ver os resultados, transformamos tb os dados de teste
# Como escalamos os dados de treino, devemos escalar os dados de test com o mesmo scaler que usamos em treino
x_test = scaler.transform(x_test)

y_pred = model.predict(x_test)

# Aqui comparamos os resultados obtidos em teste e em traino, caso sejam parecidos, isso é um bom sinal. Caso sejam muitos distantes, pode ser um sinal de overfitting
model.score(x_train, y_train)
model.score(x_test, y_test)

confusion_matrix(y_test, y_pred)

print(classification_report(y_test, y_pred))
