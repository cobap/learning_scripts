#%%

# Podemos também criar o modelo no formato Keras
from keras.layers import Dense
from keras.models import Sequential

model1 = Sequential(name='modelo_keras')
model1.add(Dense(62, input_shape=(784, ), activation='relu'))
model1.add(Dense(62, activation='relu'))
model1.add(Dense(10, activation='relu'))
model1.compile(optimizer='adam', loss='categorial_crossentropy')

# model.fit(X)
print('Modelo Keras')
model1.summary()
