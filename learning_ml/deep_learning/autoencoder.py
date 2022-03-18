
# %% [markdown]

# # Autoencoder

# ![Getting Started](https://blog.keras.io/img/ae/autoencoder_schema.jpg)


# %%

# Autoencoder livro statistics for machine learning

import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import load_digits

digits = load_digits()
X = digits.data
y = digits.target

print(X.shape)
print(y.shape)

# Normalizamos antes de criarmos qualquer rede neural
x_vars_stdscle = StandardScaler().fit_transform(X)

# %%

# Ver as imagens do nosso dataset
plt.imshow(X[11, :].reshape(8, 8), cmap='gray')
plt.title(y[11])


# %%

from keras import Model
from keras.models import Sequential
from keras.layers import Input, Dense
from keras.utils.vis_utils import plot_model

encoded = Sequential(name='encoder')
decoded = Sequential(name='decoder')
autoencoder = Sequential(name='autoencoder')

encoded.add(Dense(32, input_shape=(64,), activation='relu'))
encoded.add(Dense(16, activation='relu'))
encoded.add(Dense(2, activation='relu'))

decoded.add(Dense(16, input_shape=(2,), activation='relu'))
decoded.add(Dense(32, activation='relu'))
decoded.add(Dense(64, activation='sigmoid'))

autoencoder.add(encoded)
autoencoder.add(decoded)
autoencoder.compile(optimizer='adam', loss='mse')

# Plot do nosso modelo
plot_model(autoencoder, to_file='autoencoder_livro.png', show_shapes=True, expand_nested=True)

# Resumo do nosso modelo
autoencoder.summary(expand_nested=True)

# %%

# Treinamos a rede neural
autoencoder.fit(
    x_vars_stdscle, x_vars_stdscle,
    epochs=100,
    batch_size=256,
    shuffle=True,
    validation_split=0.2)


# %%

# Depois de treinarmos a rede, agora podemos pegar só o encoder

encoded.summary()

# Damos um freeze no treinamento
encoded.trainable = False

# Agora podemos usar livremente
reduced_X = encoded.predict(x_vars_stdscle)

print(reduced_X.shape)