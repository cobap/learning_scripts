#%%
from keras.models import Sequential
from keras.layers import Dense, Dropout

# Optimizers
from keras.optimizers import SGD

# Callbacks
from keras.callbacks import ModelCheckpoint, ReduceLROnPlateau, EarlyStopping, CSVLogger

cb_checkpoint = ModelCheckpoint(
    filepath='checkpoints/model-{epoch:02d}-{val_accuracy:.2f}.hdf5',
    monitor='val_accuracy',
    mode='max',
    save_best_only=True,
    verbose=1
)

cb_reducelr = ReduceLROnPlateau(
    monitor='val_loss',
    mode='min',
    factor=0.1,
    patience=10,
    verbose=1,
    min_lr=0.00001
)

cb_earlystop = EarlyStopping(
    monitor='val_accuracy',
    mode='max',
    min_delta=0.001,
    patience=10,
    verbose=1
)

cb_csvlogger = CSVLogger(
    filename='training_log.csv',
    separator=',',
    append=False
)

# ModelCheckpoint -> Salva um modelo para cada epoca
# tf.keras.callbacks.ModelCheckpoint

# ReduceLROnPlateau -> Reduz learning rate se tiver em plateau
# tf.keras.callbacks.ReduceLROnPlateau

# EarlyStopping -> Se a metrica não mudar em um determinado delta, termina o algoritmo
# tf.keras.callbacks.EarlyStopping

# CSVLogger
# tf.keras.callbacks.CSVLogger

# Agora criamos o modelo no keras

model = Sequential(name='modelo_keras')
model.add(Dense(62, input_shape=(784, ), activation='relu'))
model.add(Dense(62, activation='relu'))

# Se quisermos diminuir o overfitting durante treinamento, podemos adicionar um dropout
# Colocamos como parametro 20% dos neurônios desse layer
model.add(Dropout(0.2))

model.add(Dense(10, activation='relu'))
model.compile(optimizer='adam', loss='categorial_crossentropy')

# model.fit(X)
print('Modelo Keras')
model.summary()


# Keras possui dentro do SGD a implementação do learning-rate-schedule
# Podemos deixar o learning rate maior (0.001, para 0.1, mas aumentamos o momentum e colocamos um decay)
sgd = SGD(lr=0.1, momentum=0.9, decay=0.0001, nesterov=False)
# model.compile(loss='categorical_crossentropy', optimizer=sgd, metrics=['accuracy'])

model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# Aqui definimos os callbacks
historico = model.fit(X, y, epochs=100, validation_data=(X, y), callbacks=[cb_checkpoint, cb_reducelr, cb_earlystop, cb_csvlogger])

# Aqui quando pegamos o retorno do fit, temos o histórico do modelo
print(historico.history.keys())


#%%

