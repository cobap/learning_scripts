# -*- coding: utf-8 -*-

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# dataset
url = "https://community.watsonanalytics.com/wp-content/uploads/2015/04/WA_Fn-UseC_-Sales-Win-Loss.csv"
sales_data = pd.read_csv(url)


sns.set(style="whitegrid", color_codes=True)
# setting the plot size for all plots
sns.set(rc={'figure.figsize':(11.7,8.27)})
# create a countplot
sns.countplot('Route To Market',data=sales_data,hue = 'Opportunity Result')
# Remove the top and down margin
sns.despine(offset=10, trim=True)
# display the plotplt.show()

sns.violinplot(x="Opportunity Result",y="Client Size By Revenue", hue="Opportunity Result", data=sales_data);

from sklearn import preprocessing

# Transformar variáveis qualitativas em quantiativas
le = preprocessing.LabelEncoder()

sales_data['Supplies Subgroup'] = le.fit_transform(sales_data['Supplies Subgroup'])
sales_data['Region'] = le.fit_transform(sales_data['Region'])
sales_data['Route To Market'] = le.fit_transform(sales_data['Route To Market'])
sales_data['Opportunity Result'] = le.fit_transform(sales_data['Opportunity Result'])
sales_data['Competitor Type'] = le.fit_transform(sales_data['Competitor Type'])
sales_data['Supplies Group'] = le.fit_transform(sales_data['Supplies Group'])

# select columns other than 'Opportunity Number','Opportunity Result'cols = [col for col in sales_data.columns if col not in ['Opportunity Number','Opportunity Result']]
# dropping the 'Opportunity Number'and 'Opportunity Result' columns
data = sales_data[cols]
#assigning the Oppurtunity Result column as target
target = sales_data['Opportunity Result']

from sklearn.model_selection import train_test_split


# %%

# Learning about Pipeline
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.ensemble import RandomForestClassifier

# Definimos o pipeline, sempre como uma sequência de eventos. Imputer -> StandardScaler -> RandomForest
pipe = Pipeline([('imputer', SimpleImputer()),('scaler', StandardScaler()), ('RF', RandomForestClassifier())])

# Rodamos o fit no pipeline, igual fariamos com um modelo
pipe.fit(X_train, y_train)
pipe.predict(X_test)
pipe.fit_predict(X_train, y_train)


# Podemos criar um próprio estimator
from sklearn.base import BaseEstimator, TransformerMixin

# Criamos uma classe customizada do estimador
class AgeImputer(BaseEstimator, TransformerMixin):
    
    # Que tem o método init com o parametro que queremos receber
    def __init__(self, max_age):
        print('Initialising transformer...')
        self.max_age = max_age
        
    # O que acontece com o fit
    def fit(self, X, y = None):
        self.mean_age = round(X['Age'].mean())
        return self
    
    # O que fazemos com o transform
    def transform(self, X):
        print ('replacing impossible age values')
        # X.loc[(X[‘age’] > self.max_age) |  (X[‘age’] < 0), “age”] = self.mean_age
        return X