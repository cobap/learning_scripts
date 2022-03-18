# -*- coding: utf-8 -*-
"""
Script to test basic statistics using python and scikit-learn
"""

import pandas as pd
import numpy as np
from sklearn.datasets import load_boston
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats
# Label Encode string class values as integers
from sklearn.preprocessing import LabelEncoder
from scipy.stats import mannwhitneyu

from numpy.random import rand, seed, randn
from numpy import mean, var, std

boston_dataset = load_boston()

x = boston_dataset.data
y = boston_dataset.target
columns = boston_dataset.feature_names

boston_df = pd.DataFrame(boston_dataset.data)
boston_df.columns = columns

# Analise de outliers através de bloxpot
sns.boxplot(x=boston_df['DIS'])
# Necessário somente quando não estamos usando o jupyter
# plt.show()

"""
while calculating the Z-score you re-scale and center the data (mean of 0 and standard deviation of 1)
and look for the instances which are too far from zero
"""

z = np.abs(stats.zscore(boston_df))
print(z)

threshold = 3
print(np.where(z > 3))

"""
###############################################################################
"""

data = pd.read_csv("https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.data.csv", header=None)
print(data.describe())

# Count of 0 on this dataset
print((data[[1, 2, 3, 4, 5]] == 0).sum())

# Marcamos os 0s como np.NaN
data[[1, 2, 3, 4, 5]] = data[[1, 2, 3, 4, 5]].replace(0, np.NaN)

print(data.isnull().sum())

# Data strategy to fill NA is by using MEAN
data.fillna(data.mean(), inplace=True)
print(data.isnull().sum())

"""
###############################################################################
"""

iris = pd.read_csv("http://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data", header=None)
iris.head(20)

# Convert the dataframe to a numpy array
iris = iris.values

Y = iris[:, 4]

# Criamos um LabelEncoder
label_encoder = LabelEncoder()
# Iremos fazer o fit em Y
label_encoder = label_encoder.fit(Y)
# Transforma de fato os labels em numeros
label_encoded_y = label_encoder.transform(Y)

"""
###############################################################################
"""

# Criamos uma seed aleatório para poder repetir os resultados o máximo possível
seed(1)

# Criamos um dataset
data = 5 * randn(10000) + 50

print('Mean: %.3f' % mean(data))
print('Variance: %.3f' % var(data))
print('Standard Deviation: %.3f' % std(data))

# Utilizando Indian dataset
data.head()

# Tabela de score baseado no método de pearson
scoreTable = data.corr(method='pearson')

# Mostra matriz de corelação usando as variáveis
data.corr(method='pearson').style.format("{:.2}").background_gradient(cmap=plt.get_cmap('coolwarm'), axis=1)

# Generate two independent samples
data1 = 50 + (rand(100) * 10)
data2 = 51 + (rand(100) * 10)
# Compare samples
stat, p = mannwhitneyu(data1, data2)
print('Statistics = %.3f, p = %.3f' % (stat, p))
# Interpret
alpha = 0.05
if p > alpha:
    print('Same distribution (fail to reject H0)')
else:
    print('Different distribution (reject H0)')
