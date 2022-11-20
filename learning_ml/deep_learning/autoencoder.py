
# %% [markdown]

# # Autoencoder

# ![Getting Started](https://blog.keras.io/img/ae/autoencoder_schema.jpg)

#
# They are data specific. Only work with the data they were trained
#
# They are lossy, they lose information - generalization


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
from keras.layers import Input, Dense, Conv2D, MaxPooling2D, UpSampling2D
from keras.utils.vis_utils import plot_model
from keras.callbacks import TensorBoard

encoded = Sequential(name='encoder')
decoded = Sequential(name='decoder')
autoencoder = Sequential(name='autoencoder')

encoded.add(Dense(32, input_shape=(64,), activation='relu'))
encoded.add(Dense(16, activation='relu'))
encoded.add(Dense(4, activation='relu'))
encoded.add(Dense(2, activation='relu'))

decoded.add(Dense(16, input_shape=(2,), activation='relu'))
decoded.add(Dense(32, activation='relu'))
decoded.add(Dense(32, activation='relu'))
decoded.add(Dense(64, activation='sigmoid'))

autoencoder.add(Input(shape=(64,)))
autoencoder.add(encoded)
autoencoder.add(decoded)
autoencoder.compile(optimizer='adam', loss='mse')

# Plot do nosso modelo
plot_model(autoencoder, to_file='autoencoder_livro.png', show_shapes=True, expand_nested=True)

# Resumo do nosso modelo
autoencoder.summary(expand_nested=True)

# %%

# Utilizamos TensorBoard
tensorboard_callback = TensorBoard(log_dir="./logs")


# Treinamos a rede neural
autoencoder.fit(
    x_vars_stdscle, x_vars_stdscle,
    epochs=500,
    batch_size=256,
    shuffle=True,
    validation_split=0.2,
    callbacks=[tensorboard_callback])


# %%

autoencoder.predict(x_vars_stdscle[0, :].reshape(1, 64))
x_vars_stdscle[0, :]
x_vars_stdscle[0, :].reshape(1, 64)

# %%

# Depois de treinarmos a rede, agora podemos pegar só o encoder

encoded.summary()

# Damos um freeze no treinamento
encoded.trainable = False

# Agora podemos usar livremente
reduced_X = encoded.predict(x_vars_stdscle)

print(reduced_X.shape)
# %%

# Comparamos as imagens geradas com o resultado do autoencoder
n = 10  # How many digits we will display
plt.figure(figsize=(20, 4))
for i in range(n):
    # Display original
    ax = plt.subplot(2, n, i + 1)
    plt.imshow(X[i, :].reshape(8, 8))
    plt.gray()
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    # Display reconstruction
    ax = plt.subplot(2, n, i + 1 + n)
    plt.imshow(autoencoder.predict(x_vars_stdscle[i, :].reshape(1, 64)).reshape(8, 8))
    plt.gray()
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
plt.show()

# %% [markdown]

# # Convolutional Autoencoder

# 
# Same thing as a Convolutional Networks + Autoencoder
#
# Contains Conv2D and Maxpooling2D layers

conv_encoder = Sequential(name='conv_encoder')
conv_decoder = Sequential(name='conv_decoder')
conv_autoencoder = Sequential(name='conv_autoencoder')


conv_encoder.add(Conv2D(16, (3, 3), activation='relu', padding='same', input_shape=(28,28, 1)))
conv_encoder.add(MaxPooling2D((2, 2), padding='same'))
conv_encoder.add(Conv2D(8, (3, 3), activation='relu', padding='same'))
conv_encoder.add(MaxPooling2D((2, 2), padding='same'))
conv_encoder.add(Conv2D(8, (3, 3), activation='relu', padding='same'))
conv_encoder.add(MaxPooling2D((2, 2), padding='same'))

# at this point the representation is (4, 4, 8) i.e. 128-dimensional

x = conv_decoder.add(Conv2D(8, (3, 3), activation='relu', padding='same', input_shape=(4,4, 8)))
x = conv_decoder.add(UpSampling2D((2, 2)))
x = conv_decoder.add(Conv2D(8, (3, 3), activation='relu', padding='same'))
x = conv_decoder.add(UpSampling2D((2, 2)))
x = conv_decoder.add(Conv2D(16, (3, 3), activation='relu'))
x = conv_decoder.add(UpSampling2D((2, 2)))
decoded = conv_decoder.add(Conv2D(1, (3, 3), activation='sigmoid', padding='same'))

conv_autoencoder.add(conv_encoder)
conv_autoencoder.add(conv_decoder)
conv_autoencoder.compile(optimizer='adam', loss='binary_crossentropy')

# Plot do nosso modelo
plot_model(conv_autoencoder, to_file='conv_autoencoder_livro.png', show_shapes=True, expand_nested=True)

# Resumo do nosso modelo
conv_autoencoder.summary(expand_nested=True)

# %%

# Treinamos a rede neural
autoencoder.fit(
    x_vars_stdscle, x_vars_stdscle,
    epochs=500,
    batch_size=256,
    shuffle=True,
    validation_split=0.2)

# %%
