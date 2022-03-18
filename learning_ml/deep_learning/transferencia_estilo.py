#%%

import matplotlib as mpl
import matplotlib.pyplot as plt
import os
import tensorflow as tf
import numpy as np
import PIL.Image
import time
import functools
import tensorflow_hub as hub

# Definimos variável de ambiente como modelo comprimido
os.environ['TFHUB_MODEL_LOAD_FORMAT'] = 'COMPRESSED'

# Definimos configuração das imagens do matplotlib
mpl.rcParams['figure.figsize'] = (12, 12)
mpl.rcParams['axes.grid'] = False

# Transforma um tensor em uma imagem
def tensor_to_image(tensor):

    # Multiplicamos pelos 255 bits de uma imagem
    tensor = tensor*255
    tensor = np.array(tensor, dtype=np.uint8)
    if np.ndim(tensor) > 3:
        assert tensor.shape[0] == 1
        tensor = tensor[0]
    return PIL.Image.fromarray(tensor)

# %%

# Baixamos as imagens
content_path = tf.keras.utils.get_file('YellowLabradorLooking_new.jpg', 'https://storage.googleapis.com/download.tensorflow.org/example_images/YellowLabradorLooking_new.jpg')
style_path = tf.keras.utils.get_file('kandinsky5.jpg','https://storage.googleapis.com/download.tensorflow.org/example_images/Vassily_Kandinsky%2C_1913_-_Composition_7.jpg')

# %%

# Método para carregar a imagem
def load_img(path_to_img):
    max_dim = 512
    img = tf.io.read_file(path_to_img)
    img = tf.image.decode_image(img, channels=3)
    img = tf.image.convert_image_dtype(img, tf.float32)

    shape = tf.cast(tf.shape(img)[:-1], tf.float32)
    long_dim = max(shape)
    scale = max_dim / long_dim

    new_shape = tf.cast(shape * scale, tf.int32)

    img = tf.image.resize(img, new_shape)
    img = img[tf.newaxis, :]
    return img


def imshow(image, title=None):
    if len(image.shape) > 3:
        image = tf.squeeze(image, axis=0)

    plt.imshow(image)
    if title:
        plt.title(title)


# %%

content_image = load_img(content_path)
style_image = load_img(style_path)
style_image_vangogh = load_img('van_gogh.jpg')
eu = load_img('eu_em_londres.jpg')
aline = load_img('aline1.jpeg')

plt.subplot(3, 3, 1)
imshow(content_image, 'Content Image')

plt.subplot(3, 3, 2)
imshow(style_image, 'Style Image')

plt.subplot(3, 3, 3)
imshow(eu, 'Eu Londres')

plt.subplot(3, 3, 4)
imshow(style_image_vangogh, 'Van Gogh')

plt.subplot(3, 3, 5)
imshow(aline, 'Aline')


# %%

# Carregamos o modelo do tensorflow hub
hub_model = hub.load('https://tfhub.dev/google/magenta/arbitrary-image-stylization-v1-256/2')

# Aplicamos no modelo como primeiro parametro a imagem de conteúdo, e como segundo a imagem de estilo
stylized_image = hub_model(tf.constant(content_image), tf.constant(style_image))[0]

stylized_image_eu = hub_model(tf.constant(eu), tf.constant(style_image_vangogh))[0]



# Aplicamos o modelo pronto na imagem conteudo com o estilo definido
tensor_to_image(stylized_image)

# %%

eu_vangohgh = tensor_to_image(stylized_image_eu)


plt.subplot(1, 2, 1)
imshow(eu, 'Eu em Londres')
plt.subplot(1, 2, 2)
imshow(np.asarray(eu_vangohgh), 'Eu em Londres a lá Van Gogh')



# %%

# Carregamos a rede VGG19 - Very Deep Convolutional Network for Large Scale Img Recognition

# Carregamos a rede neural com a imagem de conteúdo
x = tf.keras.applications.vgg19.preprocess_input(content_image*255)
x = tf.image.resize(x, (224, 224))
vgg = tf.keras.applications.VGG19(include_top=True, weights='imagenet')
prediction_probabilities = vgg(x)
prediction_probabilities.shape

# %%

predicted_top_5 = tf.keras.applications.vgg19.decode_predictions(
    prediction_probabilities.numpy())[0]
[(class_name, prob) for (number, class_name, prob) in predicted_top_5]

# %%

# Carregamos a rede neural com a imagem de conteúdo nossa
x = tf.keras.applications.vgg19.preprocess_input(eu*255)
x = tf.image.resize(x, (224, 224))
vgg = tf.keras.applications.VGG19(include_top=True, weights='imagenet')
prediction_probabilities = vgg(x)
prediction_probabilities.shape

predicted_top_5 = tf.keras.applications.vgg19.decode_predictions(
    prediction_probabilities.numpy())[0]
[(class_name, prob) for (number, class_name, prob) in predicted_top_5]


# %%

# Agora instanciamos a rede neural sem conteúdo
vgg = tf.keras.applications.VGG19(include_top=False, weights='imagenet')

print()
# Vemos todos os layers que temos disponíveis para modificar
for layer in vgg.layers:
  print(layer.name)

# %%

# Pegamos a camada para definirmos como conteudo
content_layers = ['block5_conv2']

# E os outros blocos convolucionarios para definir o estilo
style_layers = ['block1_conv1',
                'block2_conv1',
                'block3_conv1',
                'block4_conv1',
                'block5_conv1']

num_content_layers = len(content_layers)
num_style_layers = len(style_layers)



#%%

conteudo = load_img('biden.jpg')
estilo = load_img('guernica.jpg')

plt.subplot(1, 2, 1)
imshow(conteudo)
plt.subplot(1, 2, 2)
imshow(estilo)

estilizada = hub_model(tf.constant(conteudo), tf.constant(estilo))[0]

# Aplicamos o modelo pronto na imagem conteudo com o estilo definido
tensor_to_image(estilizada)




# %%


def vgg_layers(layer_names):
    """ Creates a vgg model that returns a list of intermediate output values."""
    # Load our model. Load pretrained VGG, trained on imagenet data

    # Instanciamos o modelo pré-treinado
    vgg = tf.keras.applications.VGG19(include_top=False, weights='imagenet')

    # Colocamos como não treinável
    vgg.trainable = False

    # Para cada layer que queremos, pegamos os outputs
    outputs = [vgg.get_layer(name).output for name in layer_names]

    # Criamos um novo modelo só com os layers que queremos. Usamos o mesmo input, mas só os outputs que selecionamos
    model = tf.keras.Model([vgg.input], outputs)

    return model

# %%

# Pegamos todos os layers de estilo
style_extractor = vgg_layers(style_layers)

# Multiplicamos por 255 pois é uma imagem de estilo como output
style_outputs = style_extractor(style_image*255)

#Look at the statistics of each layer's output
for name, output in zip(style_layers, style_outputs):
  print(name)
  print("  shape: ", output.numpy().shape)
  print("  min: ", output.numpy().min())
  print("  max: ", output.numpy().max())
  print("  mean: ", output.numpy().mean())
  print()
