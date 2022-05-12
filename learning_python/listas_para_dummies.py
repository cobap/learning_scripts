from mlxtend.preprocessing import TransactionEncoder
import pandas as pd

# Identifica itens unicos
encoder = TransactionEncoder().fit(lista)

# Cria one hot
onehot = encoder.transform(lista)

# Converte onehot para dataframe
dataframe = pd.DataFrame(onehot, columns=encoder.columns_)
