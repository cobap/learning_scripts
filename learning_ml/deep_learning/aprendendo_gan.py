# Generative Adverserial Network

# https://github.com/roatienza/Deep-Learning-Experiments/blob/master/Experiments/Tensorflow/GAN/dcgan_mnist.py

#%%

import numpy as np
from keras.models import Sequential
from tensorflow.keras.optimizers import RMSprop
from keras.layers import Dense, Conv2D, LeakyReLU, Dropout, Flatten, BatchNormalization, Activation, Reshape, UpSampling2D, Conv2DTranspose

# %%

depth = 64
dropout = 0.4

# Input 28x28x1 depth = 1
# Output 14x14x1 depth = 64

input_shape = (28, 28, 1)

# %%

# Código do descriminador (recebe uma imagem e fala o quão verdadeiro a imagem é)

descriminador = Sequential(name='gan_v1_descriminador')

descriminador.add(Conv2D(depth, input_shape=input_shape, kernel_size=5,
           strides=2, padding='same', activation=LeakyReLU(alpha=0.2)))

descriminador.add(Dropout(dropout))

descriminador.add(Conv2D(depth*2, kernel_size=5, strides=2, padding='same', activation=LeakyReLU(alpha=0.2)))

descriminador.add(Dropout(dropout))

descriminador.add(Conv2D(depth*4, kernel_size=5, strides=2, padding='same', activation=LeakyReLU(alpha=0.2)))

descriminador.add(Dropout(dropout))

descriminador.add(Conv2D(depth*5, kernel_size=5, strides=2,
           padding='same', activation=LeakyReLU(alpha=0.2)))

descriminador.add(Dropout(dropout))

descriminador.add(Flatten())

descriminador.add(Dense(1, activation='sigmoid'))

descriminador.summary()


# %%

# Código do gerador, gera imagens a partir de ruido Uniforme

gerador = Sequential(name='gan_v1_gerador')

dropout = 0.4
depth = 64 * 4 #(64+64+64+64)
dim = 7

# Input 100
# Output dim x dim x depth

gerador.add(Dense(dim*dim*depth, input_dim=100))
gerador.add(BatchNormalization(momentum=0.9))
gerador.add(Activation('relu'))
gerador.add(Reshape((dim, dim, depth)))
gerador.add(Dropout(dropout))

# Input dim x dim x depth
# Output 2*dim x 2*dim x depth/2

gerador.add(UpSampling2D())
gerador.add(Conv2DTranspose(int(depth/2), 5, padding='same'))
gerador.add(BatchNormalization(momentum=0.9))
gerador.add(Activation('relu'))
gerador.add(UpSampling2D())
gerador.add(Conv2DTranspose(int(depth/4), 5, padding='same'))
gerador.add(BatchNormalization(momentum=0.9))
gerador.add(Activation('relu'))
gerador.add(Conv2DTranspose(int(depth/8), 5, padding='same'))
gerador.add(BatchNormalization(momentum=0.9))
gerador.add(Activation('relu'))

# Output: 28 x 28 x 1 grayscale image [0.0,1.0] por pix

gerador.add(Conv2DTranspose(1, 5, padding='same'))
gerador.add(Activation('sigmoid'))
gerador.summary()


# %%

# Criamos o modelo do descriminador

optimizer = RMSprop(lr=0.0008, clipvalue=1.0, decay=6e-8)
modelo_descriminator = Sequential()
modelo_descriminator.add(descriminador)
modelo_descriminator.compile(loss='binary_crossentropy', optimizer=optimizer, metrics=['accuracy'])


# %%

optimizer = RMSprop(lr=0.0004, clipvalue=1.0, decay=3e-8)
modelo_adverserial = Sequential()
modelo_adverserial.add(gerador)
modelo_adverserial.add(descriminador)
modelo_adverserial.compile(loss='binary_crossentropy', optimizer=optimizer, metrics=['accuracy'])
